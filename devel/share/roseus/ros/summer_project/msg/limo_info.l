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
  :slots (_ID _mp_dist _origin_dist _vel ))

(defmethod summer_project::limo_info
  (:init
   (&key
    ((:ID __ID) (instance std_msgs::Int64 :init))
    ((:mp_dist __mp_dist) (instance std_msgs::Float64 :init))
    ((:origin_dist __origin_dist) (instance std_msgs::Float64 :init))
    ((:vel __vel) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _ID __ID)
   (setq _mp_dist __mp_dist)
   (setq _origin_dist __origin_dist)
   (setq _vel __vel)
   self)
  (:ID
   (&rest __ID)
   (if (keywordp (car __ID))
       (send* _ID __ID)
     (progn
       (if __ID (setq _ID (car __ID)))
       _ID)))
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
  (:vel
   (&rest __vel)
   (if (keywordp (car __vel))
       (send* _vel __vel)
     (progn
       (if __vel (setq _vel (car __vel)))
       _vel)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Int64 _ID
    (send _ID :serialization-length)
    ;; std_msgs/Float64 _mp_dist
    (send _mp_dist :serialization-length)
    ;; std_msgs/Float64 _origin_dist
    (send _origin_dist :serialization-length)
    ;; std_msgs/Float64 _vel
    (send _vel :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Int64 _ID
       (send _ID :serialize s)
     ;; std_msgs/Float64 _mp_dist
       (send _mp_dist :serialize s)
     ;; std_msgs/Float64 _origin_dist
       (send _origin_dist :serialize s)
     ;; std_msgs/Float64 _vel
       (send _vel :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Int64 _ID
     (send _ID :deserialize buf ptr-) (incf ptr- (send _ID :serialization-length))
   ;; std_msgs/Float64 _mp_dist
     (send _mp_dist :deserialize buf ptr-) (incf ptr- (send _mp_dist :serialization-length))
   ;; std_msgs/Float64 _origin_dist
     (send _origin_dist :deserialize buf ptr-) (incf ptr- (send _origin_dist :serialization-length))
   ;; std_msgs/Float64 _vel
     (send _vel :deserialize buf ptr-) (incf ptr- (send _vel :serialization-length))
   ;;
   self)
  )

(setf (get summer_project::limo_info :md5sum-) "047ef4b8205d6b737a5074a1a08a0dd7")
(setf (get summer_project::limo_info :datatype-) "summer_project/limo_info")
(setf (get summer_project::limo_info :definition-)
      "std_msgs/Int64 ID
std_msgs/Float64 mp_dist
std_msgs/Float64 origin_dist
std_msgs/Float64 vel

================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :summer_project/limo_info "047ef4b8205d6b737a5074a1a08a0dd7")


