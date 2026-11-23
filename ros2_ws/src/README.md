# ROS2 packages (ROS2 Jazzy, Gazebo Harmonic)

This folder is a colcon workspace source folder. Planned packages:

| Package | Job |
|---|---|
| `robocume_description` | URDF/xacro models of mothership and scout |
| `robocume_gazebo` | Sim worlds (room with a low bed and sofa) and launch files |
| `robocume_bringup` | Launches the full stack on sim or real robots |
| `robocume_navigation` | slam_toolbox + Nav2 config, coverage planner |
| `robocume_coordinator` | Finds low zones and runs scout missions |
| `robocume_scout_bridge` | Turns `robocume_link` frames into `/scout/...` topics |

Build: `cd ros2_ws && colcon build --symlink-install`.
