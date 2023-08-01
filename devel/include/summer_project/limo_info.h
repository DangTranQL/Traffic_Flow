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
#include <std_msgs/Float64.h>
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
    , x()
    , y()
    , vel()  {
    }
  limo_info_(const ContainerAllocator& _alloc)
    : ID(_alloc)
    , x(_alloc)
    , y(_alloc)
    , vel(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Int64_<ContainerAllocator>  _ID_type;
  _ID_type ID;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _x_type;
  _x_type x;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _y_type;
  _y_type y;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _vel_type;
  _vel_type vel;





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
    lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.vel == rhs.vel;
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
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::summer_project::limo_info_<ContainerAllocator> const>
  : TrueType
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
    return "17b3f4eca66f36408d5e8a3e901190f6";
  }

  static const char* value(const ::summer_project::limo_info_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x17b3f4eca66f3640ULL;
  static const uint64_t static_value2 = 0x8d5e8a3e901190f6ULL;
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
"std_msgs/Float64 x\n"
"std_msgs/Float64 y\n"
"std_msgs/Float64 vel\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Int64\n"
"int64 data\n"
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
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.vel);
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
    s << indent << "x: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.y);
    s << indent << "vel: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.vel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SUMMER_PROJECT_MESSAGE_LIMO_INFO_H
