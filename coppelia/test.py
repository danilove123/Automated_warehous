import json

import requests
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import sim as sm
import numpy as np
import cv2

requests.delete('http://127.0.0.1:8000/warehouse/drop_tables')
requests.post('http://127.0.0.1:8000/warehouse/add_pallets')


stroke = ""
stroke_old = ""
client = RemoteAPIClient()
clientID = sm.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID == -1:
    print('Ничего не работает')
error, camera = sm.simxGetObjectHandle(clientID, "VS", sm.simx_opmode_oneshot_wait)
error, resolution, image = sm.simxGetVisionSensorImage(clientID, camera, 0, sm.simx_opmode_streaming)
sim = client.getObject('sim')
sm.simxStartSimulation(clientID, sm.simx_opmode_oneshot)
o = 0
i = 0
lst = [[2, 4], [0, 1]]
bck = 0
while (True):

    try:
        end_operation = sim.getStringSignal("end_operation")
        end_operation = sim.unpackFloatTable(end_operation)
        sim.setStringSignal("addForces", sim.packFloatTable(lst[i]))

        if end_operation[0] == 1 and bck == 0:
            i = i + 1
            bck = 1
            print("here")

        if end_operation[0] == 0:
            bck = 0


    except:
        pass
    try:
        error, resolution, image = sm.simxGetVisionSensorImage(clientID, camera, 0, sm.simx_opmode_buffer)

        if error == sm.simx_return_ok:

            ImageBGR = np.array(image).astype(np.uint8)
            ImageBGR.resize(resolution[0], resolution[1], 3)
            ImageRGB_rotated = cv2.cvtColor(ImageBGR, cv2.COLOR_BGR2RGB)

            flip_image = cv2.flip(ImageRGB_rotated, 0)
            cv2.imshow("Flip image", flip_image)

            detector = cv2.QRCodeDetector()
            data, bbox, clear_qr = detector.detectAndDecode(flip_image)

            if data != "":
                stroke = data
                if stroke_old != stroke:

                    r = requests.post(f'http://127.0.0.1:8000/warehouse/add_pallet?unparsed={data}')
                    txt = r.text
                    print(data)
                    lst[o] = [int(r.text[1]),int(r.text[2])]
                    stroke_old = stroke
                    o = o + 1


            cv2.waitKey(3)
    except:
        print("Wrong")

#print(json.loads('{"id_producer":"12238323Ktch", "type":"Kitchen","id_product_0":"12344Ktch","id_product_1":"1234Ktch","id_product_2":"112234Ktch"}'))