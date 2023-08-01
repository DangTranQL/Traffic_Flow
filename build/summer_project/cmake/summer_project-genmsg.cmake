# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "summer_project: 3 messages, 0 services")

set(MSG_I_FLAGS "-Isummer_project:/home/renan/limo_ws/src/summer_project/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(summer_project_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" NAME_WE)
add_custom_target(_summer_project_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "summer_project" "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" "std_msgs/Float64:std_msgs/Int64"
)

get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" NAME_WE)
add_custom_target(_summer_project_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "summer_project" "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" "std_msgs/Int64:std_msgs/Float64:summer_project/limo_info"
)

get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" NAME_WE)
add_custom_target(_summer_project_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "summer_project" "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" "std_msgs/Float64"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/summer_project
)
_generate_msg_cpp(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/summer_project
)
_generate_msg_cpp(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/summer_project
)

### Generating Services

### Generating Module File
_generate_module_cpp(summer_project
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/summer_project
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(summer_project_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(summer_project_generate_messages summer_project_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_cpp _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_cpp _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_cpp _summer_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(summer_project_gencpp)
add_dependencies(summer_project_gencpp summer_project_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS summer_project_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/summer_project
)
_generate_msg_eus(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/summer_project
)
_generate_msg_eus(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/summer_project
)

### Generating Services

### Generating Module File
_generate_module_eus(summer_project
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/summer_project
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(summer_project_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(summer_project_generate_messages summer_project_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_eus _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_eus _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_eus _summer_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(summer_project_geneus)
add_dependencies(summer_project_geneus summer_project_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS summer_project_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/summer_project
)
_generate_msg_lisp(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/summer_project
)
_generate_msg_lisp(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/summer_project
)

### Generating Services

### Generating Module File
_generate_module_lisp(summer_project
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/summer_project
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(summer_project_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(summer_project_generate_messages summer_project_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_lisp _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_lisp _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_lisp _summer_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(summer_project_genlisp)
add_dependencies(summer_project_genlisp summer_project_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS summer_project_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/summer_project
)
_generate_msg_nodejs(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/summer_project
)
_generate_msg_nodejs(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/summer_project
)

### Generating Services

### Generating Module File
_generate_module_nodejs(summer_project
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/summer_project
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(summer_project_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(summer_project_generate_messages summer_project_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_nodejs _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_nodejs _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_nodejs _summer_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(summer_project_gennodejs)
add_dependencies(summer_project_gennodejs summer_project_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS summer_project_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project
)
_generate_msg_py(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Int64.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg;/home/renan/limo_ws/src/summer_project/msg/limo_info.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project
)
_generate_msg_py(summer_project
  "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Float64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project
)

### Generating Services

### Generating Module File
_generate_module_py(summer_project
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(summer_project_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(summer_project_generate_messages summer_project_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_py _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/limo_info_array.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_py _summer_project_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/renan/limo_ws/src/summer_project/msg/QP_solution.msg" NAME_WE)
add_dependencies(summer_project_generate_messages_py _summer_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(summer_project_genpy)
add_dependencies(summer_project_genpy summer_project_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS summer_project_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/summer_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/summer_project
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(summer_project_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(summer_project_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/summer_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/summer_project
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(summer_project_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(summer_project_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/summer_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/summer_project
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(summer_project_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(summer_project_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/summer_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/summer_project
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(summer_project_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(summer_project_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3.8\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/summer_project
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(summer_project_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(summer_project_generate_messages_py std_msgs_generate_messages_py)
endif()
