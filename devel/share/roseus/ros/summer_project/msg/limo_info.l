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
  :slots (_ID _x _y _vel _acc ))

(defmethod summer_project::limo_info
  (:init
   (&key
    ((:ID __ID) (instance std_msgs::Int64 :init))
    ((:x __x) (instance std_msgs::Float64 :init))
    ((:y __y) (instance std_msgs::Float64 :init))
    ((:vel __vel) (instance std_msgs::Float64 :init))
    ((:acc __acc) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _ID __ID)
   (setq _x __x)
   (setq _y __y)
   (setq _vel __vel)
   (setq _acc __acc)
   self)
  (:ID
   (&rest __ID)
   (if (keywordp (car __ID))
       (send* _ID __ID)
     (progn
       (if __ID (setq _ID (car __ID)))
       _ID)))
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
  (:vel
   (&rest __vel)
   (if (keywordp (car __vel))
       (send* _vel __vel)
     (progn
       (if __vel (setq _vel (car __vel)))
       _vel)))
  (:acc
   (&rest __acc)
   (if (keywordp (car __acc))
       (send* _acc __acc)
     (progn
       (if __acc (setq _acc (car __acc)))
       _acc)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Int64 _ID
    (send _ID :serialization-length)
    ;; std_msgs/Float64 _x
    (send _x :serialization-length)
    ;; std_msgs/Float64 _y
    (send _y :serialization-length)
    ;; std_msgs/Float64 _vel
    (send _vel :serialization-length)
    ;; std_msgs/Float64 _acc
    (send _acc :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Int64 _ID
       (send _ID :serialize s)
     ;; std_msgs/Float64 _x
       (send _x :serialize s)
     ;; std_msgs/Float64 _y
       (send _y :serialize s)
     ;; std_msgs/Float64 _vel
       (send _vel :serialize s)
     ;; std_msgs/Float64 _acc
       (send _acc :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Int64 _ID
     (send _ID :deserialize buf ptr-) (incf ptr- (send _ID :serialization-length))
   ;; std_msgs/Float64 _x
     (send _x :deserialize buf ptr-) (incf ptr- (send _x :serialization-length))
   ;; std_msgs/Float64 _y
     (send _y :deserialize buf ptr-) (incf ptr- (send _y :serialization-length))
   ;; std_msgs/Float64 _vel
     (send _vel :deserialize buf ptr-) (incf ptr- (send _vel :serialization-length))
   ;; std_msgs/Float64 _acc
     (send _acc :deserialize buf ptr-) (incf ptr- (send _acc :serialization-length))
   ;;
   self)
  )

(setf (get summer_project::limo_info :md5sum-) "326e2462ad523a29cf0e1a6ca744aac8")
(setf (get summer_project::limo_info :datatype-) "summer_project/limo_info")
(setf (get summer_project::limo_info :definition-)
      "std_msgs/Int64 ID
std_msgs/Float64 x
std_msgs/Float64 y
std_msgs/Float64 vel
std_msgs/Float64 acc

================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :summer_project/limo_info "326e2462ad523a29cf0e1a6ca744aac8")


