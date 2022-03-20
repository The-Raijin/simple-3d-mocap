import mediapipe as mp
import cv2

file = 'data/input-video/gangnam_style_dance_class.mp4'
cap = cv2.VideoCapture(file)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose
landmarks_list = []

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    while True: #cap.isOpened():

        success, frame = cap.read()

        if not success:
            print('Ignoring empty frame.')
        # If loading a video, use 'break' instead of 'continue'.
            break
        
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.q
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = pose.process(frame)

        if not results.pose_landmarks:
            continue
        
        # Draw landmarks and show image
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        
        cv2.imshow('Pose', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
# cv2.destroyAllWindows()


