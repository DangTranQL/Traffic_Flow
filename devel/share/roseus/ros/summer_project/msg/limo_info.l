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
  :slots (_ID _pose _vel _accel ))

(defmethod summer_project::limo_info
  (:init
   (&key
    ((:ID __ID) (instance std_msgs::Int64 :init))
    ((:pose __pose) (instance std_msgs::Float64MultiArray :init))
    ((:vel __vel) (instance std_msgs::Float64 :init))
    ((:accel __accel) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _ID __ID)
   (setq _pose __pose)
   (setq _vel __vel)
   (setq _accel __accel)
   self)
  (:ID
   (&rest __ID)
   (if (keywordp (car __ID))
       (send* _ID __ID)
     (progn
       (if __ID (setq _ID (car __ID)))
       _ID)))
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:vel
   (&rest __vel)
   (if (keywordp (car __vel))
       (send* _vel __vel)
     (progn
       (if __vel (setq _vel (car __vel)))
       _vel)))
  (:accel
   (&rest __accel)
   (if (keywordp (car __accel))
       (send* _accel __accel)
     (progn
       (if __accel (setq _accel (car __accel)))
       _accel)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Int64 _ID
    (send _ID :serialization-length)
    ;; std_msgs/Float64MultiArray _pose
    (send _pose :serialization-length)
    ;; std_msgs/Float64 _vel
    (send _vel :serialization-length)
    ;; std_msgs/Float64 _accel
    (send _accel :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Int64 _ID
       (send _ID :serialize s)
     ;; std_msgs/Float64MultiArray _pose
       (send _pose :serialize s)
     ;; std_msgs/Float64 _vel
       (send _vel :serialize s)
     ;; std_msgs/Float64 _accel
       (send _accel :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Int64 _ID
     (send _ID :deserialize buf ptr-) (incf ptr- (send _ID :serialization-length))
   ;; std_msgs/Float64MultiArray _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;; std_msgs/Float64 _vel
     (send _vel :deserialize buf ptr-) (incf ptr- (send _vel :serialization-length))
   ;; std_msgs/Float64 _accel
     (send _accel :deserialize buf ptr-) (incf ptr- (send _accel :serialization-length))
   ;;
   self)
  )

(setf (get summer_project::limo_info :md5sum-) "68fc7bffa679ec42e202fe8ddecc03a6")
(setf (get summer_project::limo_info :datatype-) "summer_project/limo_info")
(setf (get summer_project::limo_info :definition-)
      "std_msgs/Int64 ID
std_msgs/Float64MultiArray pose
std_msgs/Float64 vel
std_msgs/Float64 accel

================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
float64[]         data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = \"height\"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = \"width\"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = \"channel\"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension
================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :summer_project/limo_info "68fc7bffa679ec42e202fe8ddecc03a6")


