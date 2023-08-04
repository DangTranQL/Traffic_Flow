;; Auto-generated. Do not edit!


(when (boundp 'summer_project::limo_info)
  (if (not (find-package "SUMMER_PROJECT"))
    (make-package "SUMMER_PROJECT"))
  (shadow 'limo_info (find-package "SUMMER_PROJECT")))
(unless (find-package "SUMMER_PROJECT::LIMO_INFO")
  (make-package "SUMMER_PROJECT::LIMO_INFO"))

(in-package "ROS")
;;//! \htmlinclude limo_info.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass summer_project::limo_info
  :super ros::object
  :slots (_ID _vel _x _y _mp_dist _origin_dist _path _d1 _d2 ))

(defmethod summer_project::limo_info
  (:init
   (&key
    ((:ID __ID) (instance std_msgs::Int64 :init))
    ((:vel __vel) (instance std_msgs::Float64 :init))
    ((:x __x) (instance std_msgs::Float64 :init))
    ((:y __y) (instance std_msgs::Float64 :init))
    ((:mp_dist __mp_dist) (instance std_msgs::Float64 :init))
    ((:origin_dist __origin_dist) (instance std_msgs::Float64 :init))
    ((:path __path) (instance std_msgs::String :init))
    ((:d1 __d1) (instance std_msgs::Float64 :init))
    ((:d2 __d2) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _ID __ID)
   (setq _vel __vel)
   (setq _x __x)
   (setq _y __y)
   (setq _mp_dist __mp_dist)
   (setq _origin_dist __origin_dist)
   (setq _path __path)
   (setq _d1 __d1)
   (setq _d2 __d2)
   self)
  (:ID
   (&rest __ID)
   (if (keywordp (car __ID))
       (send* _ID __ID)
     (progn
       (if __ID (setq _ID (car __ID)))
       _ID)))
  (:vel
   (&rest __vel)
   (if (keywordp (car __vel))
       (send* _vel __vel)
     (progn
       (if __vel (setq _vel (car __vel)))
       _vel)))
  (:x
   (&rest __x)
   (if (keywordp (car __x))
       (send* _x __x)
     (progn
       (if __x (setq _x (car __x)))
       _x)))
  (:y
   (&rest __y)
   (if (keywordp (car __y))
       (send* _y __y)
     (progn
       (if __y (setq _y (car __y)))
       _y)))
  (:mp_dist
   (&rest __mp_dist)
   (if (keywordp (car __mp_dist))
       (send* _mp_dist __mp_dist)
     (progn
       (if __mp_dist (setq _mp_dist (car __mp_dist)))
       _mp_dist)))
  (:origin_dist
   (&rest __origin_dist)
   (if (keywordp (car __origin_dist))
       (send* _origin_dist __origin_dist)
     (progn
       (if __origin_dist (setq _origin_dist (car __origin_dist)))
       _origin_dist)))
  (:path
   (&rest __path)
   (if (keywordp (car __path))
       (send* _path __path)
     (progn
       (if __path (setq _path (car __path)))
       _path)))
  (:d1
   (&rest __d1)
   (if (keywordp (car __d1))
       (send* _d1 __d1)
     (progn
       (if __d1 (setq _d1 (car __d1)))
       _d1)))
  (:d2
   (&rest __d2)
   (if (keywordp (car __d2))
       (send* _d2 __d2)
     (progn
       (if __d2 (setq _d2 (car __d2)))
       _d2)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Int64 _ID
    (send _ID :serialization-length)
    ;; std_msgs/Float64 _vel
    (send _vel :serialization-length)
    ;; std_msgs/Float64 _x
    (send _x :serialization-length)
    ;; std_msgs/Float64 _y
    (send _y :serialization-length)
    ;; std_msgs/Float64 _mp_dist
    (send _mp_dist :serialization-length)
    ;; std_msgs/Float64 _origin_dist
    (send _origin_dist :serialization-length)
    ;; std_msgs/String _path
    (send _path :serialization-length)
    ;; std_msgs/Float64 _d1
    (send _d1 :serialization-length)
    ;; std_msgs/Float64 _d2
    (send _d2 :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Int64 _ID
       (send _ID :serialize s)
     ;; std_msgs/Float64 _vel
       (send _vel :serialize s)
     ;; std_msgs/Float64 _x
       (send _x :serialize s)
     ;; std_msgs/Float64 _y
       (send _y :serialize s)
     ;; std_msgs/Float64 _mp_dist
       (send _mp_dist :serialize s)
     ;; std_msgs/Float64 _origin_dist
       (send _origin_dist :serialize s)
     ;; std_msgs/String _path
       (send _path :serialize s)
     ;; std_msgs/Float64 _d1
       (send _d1 :serialize s)
     ;; std_msgs/Float64 _d2
       (send _d2 :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Int64 _ID
     (send _ID :deserialize buf ptr-) (incf ptr- (send _ID :serialization-length))
   ;; std_msgs/Float64 _vel
     (send _vel :deserialize buf ptr-) (incf ptr- (send _vel :serialization-length))
   ;; std_msgs/Float64 _x
     (send _x :deserialize buf ptr-) (incf ptr- (send _x :serialization-length))
   ;; std_msgs/Float64 _y
     (send _y :deserialize buf ptr-) (incf ptr- (send _y :serialization-length))
   ;; std_msgs/Float64 _mp_dist
     (send _mp_dist :deserialize buf ptr-) (incf ptr- (send _mp_dist :serialization-length))
   ;; std_msgs/Float64 _origin_dist
     (send _origin_dist :deserialize buf ptr-) (incf ptr- (send _origin_dist :serialization-length))
   ;; std_msgs/String _path
     (send _path :deserialize buf ptr-) (incf ptr- (send _path :serialization-length))
   ;; std_msgs/Float64 _d1
     (send _d1 :deserialize buf ptr-) (incf ptr- (send _d1 :serialization-length))
   ;; std_msgs/Float64 _d2
     (send _d2 :deserialize buf ptr-) (incf ptr- (send _d2 :serialization-length))
   ;;
   self)
  )

(setf (get summer_project::limo_info :md5sum-) "24e962fd472c2ad4988156ac52134873")
(setf (get summer_project::limo_info :datatype-) "summer_project/limo_info")
(setf (get summer_project::limo_info :definition-)
      "std_msgs/Int64 ID
std_msgs/Float64 vel
std_msgs/Float64 x
std_msgs/Float64 y
std_msgs/Float64 mp_dist
std_msgs/Float64 origin_dist
std_msgs/String path

std_msgs/Float64 d1
std_msgs/Float64 d2

================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data
================================================================================
MSG: std_msgs/String
string data

")



(provide :summer_project/limo_info "24e962fd472c2ad4988156ac52134873")


