#!/usr/bin/env python
import marlo
from marlo import MarloEnvBuilderBase
from marlo import MalmoPython


import os
from pathlib import Path


class MarloEnvBuilder(MarloEnvBuilderBase):
    """
    Description:
		The goal of this mission is for the agent to eat commestible food
		and avoid to eat dangerous items.

	Actions available:
		Move forward/backward
		Jump
		Turn
		Strafe
		Crouch
		Use

	Rewards: 
		either + 1 or +2 when collecting food
		-2 when collecting dangerous items
    """
    
    def __init__(self, extra_params={}):
        super(MarloEnvBuilder, self).__init__(
                templates_folder = os.path.join(
                            Path(__file__).parent,
                            "templates"
                )
        )
        self.params = self._default_params()
        # You can do something with the extra_params if you wish
        self.params.update(extra_params)

    def _default_params(self):
        _default_params = super(MarloEnvBuilder, self).default_base_params
        _default_params.update(
            dict(
                tick_length=50,
                agent_names=["MarLo-agent0"],
                episode_timelimit=60000
            )
        )
        return _default_params

    def render_mission_spec(self):
        """
        TODO: Randomize  location of food items
        """
        template = self.jinj2_env.get_template("mission.xml")
        return template.render(
            params=self.params
        )


if __name__ == "__main__":
    env_builder =  MarloEnvBuilder()
    print(env_builder.params)
    print(env_builder.params.experiment_id)
    mission_xml = env_builder.render_mission_spec()
    mission_spec = MalmoPython.MissionSpec(mission_xml, True)
    print(mission_spec.getSummary())
