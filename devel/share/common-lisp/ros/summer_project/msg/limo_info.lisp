; Auto-generated. Do not edit!


(cl:in-package summer_project-msg)


;//! \htmlinclude limo_info.msg.html

(cl:defclass <limo_info> (roslisp-msg-protocol:ros-message)
  ((ID
    :reader ID
    :initarg :ID
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64))
   (mp_dist
    :reader mp_dist
    :initarg :mp_dist
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (origin_dist
    :reader origin_dist
    :initarg :origin_dist
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (vel
    :reader vel
    :initarg :vel
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (path
    :reader path
    :initarg :path
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String)))
)

(cl:defclass limo_info (<limo_info>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <limo_info>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'limo_info)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name summer_project-msg:<limo_info> is deprecated: use summer_project-msg:limo_info instead.")))

(cl:ensure-generic-function 'ID-val :lambda-list '(m))
(cl:defmethod ID-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:ID-val is deprecated.  Use summer_project-msg:ID instead.")
  (ID m))

(cl:ensure-generic-function 'mp_dist-val :lambda-list '(m))
(cl:defmethod mp_dist-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:mp_dist-val is deprecated.  Use summer_project-msg:mp_dist instead.")
  (mp_dist m))

(cl:ensure-generic-function 'origin_dist-val :lambda-list '(m))
(cl:defmethod origin_dist-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:origin_dist-val is deprecated.  Use summer_project-msg:origin_dist instead.")
  (origin_dist m))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:vel-val is deprecated.  Use summer_project-msg:vel instead.")
  (vel m))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:path-val is deprecated.  Use summer_project-msg:path instead.")
  (path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <limo_info>) ostream)
  "Serializes a message object of type '<limo_info>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'mp_dist) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'origin_dist) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vel) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'path) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <limo_info>) istream)
  "Deserializes a message object of type '<limo_info>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'mp_dist) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'origin_dist) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vel) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'path) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<limo_info>)))
  "Returns string type for a message object of type '<limo_info>"
  "summer_project/limo_info")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'limo_info)))
  "Returns string type for a message object of type 'limo_info"
  "summer_project/limo_info")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<limo_info>)))
  "Returns md5sum for a message object of type '<limo_info>"
  "d8ca2cf53c0b774c7306231e90ca8a64")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'limo_info)))
  "Returns md5sum for a message object of type 'limo_info"
  "d8ca2cf53c0b774c7306231e90ca8a64")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<limo_info>)))
  "Returns full string definition for message of type '<limo_info>"
  (cl:format cl:nil "std_msgs/Int64 ID~%std_msgs/Float64 mp_dist~%std_msgs/Float64 origin_dist~%std_msgs/Float64 vel~%std_msgs/String path~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'limo_info)))
  "Returns full string definition for message of type 'limo_info"
  (cl:format cl:nil "std_msgs/Int64 ID~%std_msgs/Float64 mp_dist~%std_msgs/Float64 origin_dist~%std_msgs/Float64 vel~%std_msgs/String path~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <limo_info>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'mp_dist))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'origin_dist))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vel))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <limo_info>))
  "Converts a ROS message object to a list"
  (cl:list 'limo_info
    (cl:cons ':ID (ID msg))
    (cl:cons ':mp_dist (mp_dist msg))
    (cl:cons ':origin_dist (origin_dist msg))
    (cl:cons ':vel (vel msg))
    (cl:cons ':path (path msg))
))
