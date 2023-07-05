; Auto-generated. Do not edit!


(cl:in-package summer_project-msg)


;//! \htmlinclude limo_info.msg.html

(cl:defclass <limo_info> (roslisp-msg-protocol:ros-message)
  ((ID
    :reader ID
    :initarg :ID
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64))
   (pose
    :reader pose
    :initarg :pose
    :type std_msgs-msg:Float64MultiArray
    :initform (cl:make-instance 'std_msgs-msg:Float64MultiArray))
   (vel
    :reader vel
    :initarg :vel
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (accel
    :reader accel
    :initarg :accel
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64)))
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

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:pose-val is deprecated.  Use summer_project-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:vel-val is deprecated.  Use summer_project-msg:vel instead.")
  (vel m))

(cl:ensure-generic-function 'accel-val :lambda-list '(m))
(cl:defmethod accel-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:accel-val is deprecated.  Use summer_project-msg:accel instead.")
  (accel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <limo_info>) ostream)
  "Serializes a message object of type '<limo_info>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vel) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'accel) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <limo_info>) istream)
  "Deserializes a message object of type '<limo_info>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vel) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'accel) istream)
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
  "68fc7bffa679ec42e202fe8ddecc03a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'limo_info)))
  "Returns md5sum for a message object of type 'limo_info"
  "68fc7bffa679ec42e202fe8ddecc03a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<limo_info>)))
  "Returns full string definition for message of type '<limo_info>"
  (cl:format cl:nil "std_msgs/Int64 ID~%std_msgs/Float64MultiArray pose~%std_msgs/Float64 vel~%std_msgs/Float64 accel~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float64[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'limo_info)))
  "Returns full string definition for message of type 'limo_info"
  (cl:format cl:nil "std_msgs/Int64 ID~%std_msgs/Float64MultiArray pose~%std_msgs/Float64 vel~%std_msgs/Float64 accel~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float64[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <limo_info>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vel))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'accel))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <limo_info>))
  "Converts a ROS message object to a list"
  (cl:list 'limo_info
    (cl:cons ':ID (ID msg))
    (cl:cons ':pose (pose msg))
    (cl:cons ':vel (vel msg))
    (cl:cons ':accel (accel msg))
))
