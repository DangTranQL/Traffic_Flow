;; Auto-generated. Do not edit!


(when (boundp 'summer_project::limo_info_array)
  (if (not (find-package "SUMMER_PROJECT"))
    (make-package "SUMMER_PROJECT"))
  (shadow 'limo_info_array (find-package "SUMMER_PROJECT")))
(unless (find-package "SUMMER_PROJECT::LIMO_INFO_ARRAY")
  (make-package "SUMMER_PROJECT::LIMO_INFO_ARRAY"))

(in-package "ROS")
;;//! \htmlinclude limo_info_array.msg.html


(defclass summer_project::limo_info_array
  :super ros::object
  :slots (_limo_infos ))

(defmethod summer_project::limo_info_array
  (:init
   (&key
    ((:limo_infos __limo_infos) ())
    )
   (send-super :init)
   (setq _limo_infos __limo_infos)
   self)
  (:limo_infos
   (&rest __limo_infos)
   (if (keywordp (car __limo_infos))
       (send* _limo_infos __limo_infos)
     (progn
       (if __limo_infos (setq _limo_infos (car __limo_infos)))
       _limo_infos)))
  (:serialization-length
   ()
   (+
    ;; summer_project/limo_info[] _limo_infos
    (apply #'+ (send-all _limo_infos :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; summer_project/limo_info[] _limo_infos
     (write-long (length _limo_infos) s)
     (dolist (elem _limo_infos)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; summer_project/limo_info[] _limo_infos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _limo_infos (let (r) (dotimes (i n) (push (instance summer_project::limo_info :init) r)) r))
     (dolist (elem- _limo_infos)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get summer_project::limo_info_array :md5sum-) "053fded398d0eae04d5110e91390f4be")
(setf (get summer_project::limo_info_array :datatype-) "summer_project/limo_info_array")
(setf (get summer_project::limo_info_array :definition-)
      "limo_info[] limo_infos

================================================================================
MSG: summer_project/limo_info
std_msgs/Int64 ID
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



(provide :summer_project/limo_info_array "053fded398d0eae04d5110e91390f4be")


