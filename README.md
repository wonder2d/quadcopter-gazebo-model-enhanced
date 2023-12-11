# quadcopter-gazebo-model-enhanced
Enhanced Gazebo model of a quadcopter enabling the creation of world with multiple instances.

This project is an enhanced quadcopter model for Gazebo.
It's an updated version of the example Gazebo quadcopter model, located in: 
/usr/share/gazebo-5.3/worlds/quad_rotor_demo.world

The use case for this model was multi-robot collaboration/swarms.
So wonder2d wanted to have a world where they could ideally spawn multiple instances of a single model.
However there were difficulties in achieving this in Gazebo.
So a different approach was taken, where a temp