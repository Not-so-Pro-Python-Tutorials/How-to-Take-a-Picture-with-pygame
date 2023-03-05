import pygame.camera
import time

pygame.camera.init()

camlist = pygame.camera.list_cameras()

if camlist:
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()

    time.sleep(2)

    pic = cam.get_image()
    pygame.image.save(pic, "image.jpg")
else:
    print("No camera detected.")
