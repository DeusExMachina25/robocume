# Developer setup

## Right now (Phase 0)
Only the `robocume_link` Python package has code:

```bash
cd software/robocume_link
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

## Coming in Phase 1: ROS2 + Gazebo on an 8 GB laptop
ROS2 Jazzy and Gazebo Harmonic want Ubuntu 24.04. With 8 GB of RAM:
- Run Gazebo **headless** (`gz sim -s`) and view it in RViz, or use the lighter
  test world. The full 3D GUI is the biggest memory user.
- Add an 8 GB swap file on Linux, or give WSL2 at least 6 GB on Windows.
- Close the browser while simulating.
- A Docker image will be provided so setup is one command on any OS.
