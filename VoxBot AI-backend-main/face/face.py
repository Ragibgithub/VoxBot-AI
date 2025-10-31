import cv2
import face_recognition

def face():
    known_faces = {
        "Ragib": face_recognition.load_image_file("face/image/1.jpg"),
        "gungun": face_recognition.load_image_file("face/image/2.jpg"),
        "gungun": face_recognition.load_image_file("face/image/3.jpg"),
        "tani":face_recognition.load_image_file("face/image/4.jpg"),
        "tani":face_recognition.load_image_file("face/image/5.jpg"),
        "tani":face_recognition.load_image_file("face/image/6.jpg"),
    }

    known_face_encodings = {name: face_recognition.face_encodings(image)[0] for name, image in known_faces.items()}

    video_capture = cv2.VideoCapture(0)

    locked = True
    i = 0

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("Failed to capture frame")
            break

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        if not face_locations:
            locked = True

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(list(known_face_encodings.values()), face_encoding)

            if True in matches:
                locked = False
                name = list(known_face_encodings.keys())[matches.index(True)]
            else:
                locked = True
                name = "Unknown"

            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 4)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Face Lock', frame)

        if locked:
            i += 1
            if i >= 30:  # Change the condition to break after 30 attempts
                video_capture.release()
                cv2.destroyWindow('Face Lock')
                return "unknown", 0
        else:
            print("Access Granted!")
            if name == "Ragib":
                video_capture.release()
                cv2.destroyWindow('Face Lock')
                return name, 2
            video_capture.release()
            cv2.destroyWindow('Face Lock')
            return name, 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

