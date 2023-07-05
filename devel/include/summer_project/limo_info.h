// Generated by gencpp from file summer_project/limo_info.msg
// DO NOT EDIT!


#ifndef SUMMER_PROJECT_MESSAGE_LIMO_INFO_H
#define SUMMER_PROJECT_MESSAGE_LIMO_INFO_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Int64.h>
#include <std_msgs/Float64MultiArray.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>

namespace summer_project
{
template <class ContainerAllocator>
struct limo_info_
{
  typedef limo_info_<ContainerAllocator> Type;

  limo_info_()
    : ID()
    , pose()
    , vel()
    , accel()  {
    }
  limo_info_(const ContainerAllocator& _alloc)
    : ID(_alloc)
    , pose(_alloc)
    , vel(_alloc)
    , accel(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Int64_<ContainerAllocator>  _ID_type;
  _ID_type ID;

   typedef  ::std_msgs::Float64MultiArray_<ContainerAllocator>  _pose_type;
  _pose_type pose;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _vel_type;
  _vel_type vel;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _accel_type;
  _accel_type accel;





  typedef boost::shared_ptr< ::summer_project::limo_info_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::summer_project::limo_info_<ContainerAllocator> const> ConstPtr;

}; // struct limo_info_

typedef ::summer_project::limo_info_<std::allocator<void> > limo_info;

typedef boost::shared_ptr< ::summer_project::limo_info > limo_infoPtr;
typedef boost::shared_ptr< ::summer_project::limo_info const> limo_infoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::summer_project::limo_info_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::summer_project::limo_info_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::summer_project::limo_info_<ContainerAllocator1> & lhs, const ::summer_project::limo_info_<ContainerAllocator2> & rhs)
{
  return lhs.ID == rhs.ID &&
    lhs.pose == rhs.pose &&
    lhs.vel == rhs.vel &&
    lhs.accel == rhs.accel;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::summer_project::limo_info_<ContainerAllocator1> & lhs, const ::summer_project::limo_info_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace summer_project

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::summer_project::limo_info_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::summer_project::limo_info_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::summer_project::limo_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::summer_project::limo_info_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::summer_project::limo_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::summer_project::limo_info_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::summer_project::limo_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "68fc7bffa679ec42e202fe8ddecc03a6";
  }

  static const char* value(const ::summer_project::limo_info_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x68fc7bffa679ec42ULL;
  static const uint64_t static_value2 = 0xe202fe8ddecc03a6ULL;
};

template<class ContainerAllocator>
struct DataType< ::summer_project::limo_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "summer_project/limo_info";
  }

  static const char* value(const ::summer_project::limo_info_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::summer_project::limo_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Int64 ID\n"
"std_msgs/Float64MultiArray pose\n"
"std_msgs/Float64 vel\n"
"std_msgs/Float64 accel\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Int64\n"
"int64 data\n"
"================================================================================\n"
"MSG: std_msgs/Float64MultiArray\n"
"# Please look at the MultiArrayLayout message definition for\n"
"# documentation on all multiarrays.\n"
"\n"
"MultiArrayLayout  layout        # specification of data layout\n"
"float64[]         data          # array of data\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/MultiArrayLayout\n"
"# The multiarray declares a generic multi-dimensional array of a\n"
"# particular data type.  Dimensions are ordered from outer most\n"
"# to inner most.\n"
"\n"
"MultiArrayDimension[] dim # Array of dimension properties\n"
"uint32 data_offset        # padding elements at front of data\n"
"\n"
"# Accessors should ALWAYS be written in terms of dimension stride\n"
"# and specified outer-most dimension first.\n"
"# \n"
"# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n"
"#\n"
"# A standard, 3-channel 640x480 image with interleaved color channels\n"
"# would be specified as:\n"
"#\n"
"# dim[0].label  = \"height\"\n"
"# dim[0].size   = 480\n"
"# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n"
"# dim[1].label  = \"width\"\n"
"# dim[1].size   = 640\n"
"# dim[1].stride = 3*640 = 1920\n"
"# dim[2].label  = \"channel\"\n"
"# dim[2].size   = 3\n"
"# dim[2].stride = 3\n"
"#\n"
"# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/MultiArrayDimension\n"
"string label   # label of given dimension\n"
"uint32 size    # size of given dimension (in type units)\n"
"uint32 stride  # stride of given dimension\n"
"================================================================================\n"
"MSG: std_msgs/Float64\n"
"float64 data\n"
;
  }

  static const char* value(const ::summer_project::limo_info_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::summer_project::limo_info_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ID);
      stream.next(m.pose);
      stream.next(m.vel);
      stream.next(m.accel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct limo_info_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::summer_project::limo_info_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::summer_project::limo_info_<ContainerAllocator>& v)
  {
    s << indent << "ID: ";
    s << std::endl;
    Printer< ::std_msgs::Int64_<ContainerAllocator> >::stream(s, indent + "  ", v.ID);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::std_msgs::Float64MultiArray_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
    s << indent << "vel: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.vel);
    s << indent << "accel: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.accel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SUMMER_PROJECT_MESSAGE_LIMO_INFO_H
