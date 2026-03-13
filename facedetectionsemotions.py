import cv2
import mediapipe as mp
from deepface import DeepFace
import time

class FaceDetector:
    def __init__(self):
        self.mpFace = mp.solutions.face_detection
        self.fd = self.mpFace.FaceDetection(min_detection_confidence=0.80)

    def FindFace(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.fd.process(imgRGB)
        bboxs = []
        if self.results.detections:
            for id, detec in enumerate(self.results.detections):
                bboxC = detec.location_data.relative_bounding_box
                h, w, c = img.shape

                bbox = (
                    int(bboxC.xmin * w),
                    int(bboxC.ymin * h),
                    int(bboxC.width * w),
                    int(bboxC.height * h),
                )

                bboxs.append([id, bbox, detec.score])
                cv2.rectangle(img, bbox, (225, 0, 255), 2)

        return img, bboxs


def predict_emotion(face_img):
    try:
        result = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)

        # DeepFace may return list
        if isinstance(result, list):
            result = result[0]

        emotion = result["dominant_emotion"]
        confidence = result["emotion"][emotion]

        return f"{emotion} ({confidence:.1f}%)"

    except Exception as e:
        print("Emotion detection error:", e)
        return "Unknown"


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()

    prev_time = 0

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image.")
            break

        img, bboxs = detector.FindFace(img)

        if bboxs:
            for bbox_info in bboxs:
                bbox = bbox_info[1]
                x, y, w, h = bbox

                h_img, w_img, _ = img.shape
                x, y = max(0, x), max(0, y)
                x2, y2 = min(x + w, w_img), min(y + h, h_img)

                face_img = cv2.resize(img[y:y2, x:x2], (224, 224))

                current_time = time.time()

                if face_img.size > 0 and current_time - prev_time > 1:
                    prev_time = current_time
                    emotion = predict_emotion(face_img)

                    cv2.putText(
                        img,
                        emotion,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_PLAIN,
                        2,
                        (0, 255, 0),
                        2,
                    )

        
        text = "DEV BY ALUVALA EDIGA HARSHA VARDHAN GOUD"
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.4
        thickness = 1

        (text_width, text_height), _ = cv2.getTextSize(text, font, scale, thickness)

        x = (img.shape[1] - text_width) // 2
        y = img.shape[0] - 10

        cv2.putText(
            img,
            text,
            (x, y),
            font,
            scale,
            (255, 255, 255),
            thickness,
            cv2.LINE_AA,
        )
        # ----------------------------------------

        cv2.imshow("Emotion Detection", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

