import random


class World:

    def __init__(self):

        # 地图区域
        self.regions = {
            "青云域": {
                "description": "正道宗门管辖的和平区域",
                "locations": ["青云城", "青云宗", "青云镇"]
            },
            "黑风域": {
                "description": "魔道势力控制的混乱区域",
                "locations": ["黑风山", "血刀门", "万魔渊"]
            },
            "荒域": {
                "description": "危险的野外区域",
                "locations": ["落日森林", "死亡沙漠", "寒冰峡谷"]
            }
        }

        # 城镇（详细设定）
        self.towns = {
            "青云城": {
                "description": "青云域的主城，繁荣安定",
                "faction": "青云宗",
                "resources": ["药材", "矿石", "功法"],
                "danger_level": 1
            },
            "黑风山": {
                "description": "魔道聚集地，危机四伏",
                "faction": "血刀门",
                "resources": ["魔核", "毒草"],
                "danger_level": 5
            },
            "落日森林": {
                "description": "妖兽横行的原始森林",
                "faction": None,
                "resources": ["灵兽", "天材地宝"],
                "danger_level": 4
            }
        }

        # 势力
        self.factions = {
            "青云宗": {
                "type": "正道",
                "description": "名门正派，以斩妖除魔为己任",
                "power": 80
            },
            "血刀门": {
                "type": "魔道",
                "description": "修炼魔功的邪恶门派",
                "power": 60
            },
            "散修联盟": {
                "type": "中立",
                "description": "散修组成的松散组织",
                "power": 40
            }
        }

        # 资源类型
        self.resource_types = [
            "药材", "矿石", "灵兽", "魔核",
            "功法", "法宝", "天材地宝"
        ]

        # 世界状态
        self.time = 0
        self.weather = "晴朗"
        self.global_events = []

    def get_random_location(self):
        """随机获取一个地点"""
        locations = []
        for region in self.regions.values():
            locations.extend(region["locations"])
        return random.choice(locations)

    def get_locations_by_faction(self, faction):
        """获取某个势力控制的所有地点"""
        return [
            name for name, info in self.towns.items()
            if info.get("faction") == faction
        ]

    def get_location_info(self, location_name):
        """获取地点详细信息"""
        return self.towns.get(location_name, {})

    def get_random_resource(self):
        """随机获取一种资源"""
        return random.choice(self.resource_types)

    def advance_time(self):
        """推进世界时间"""
        self.time += 1
        weathers = ["晴朗", "多云", "小雨", "暴雨", "大风", "大雾"]
        self.weather = random.choice(weathers)

    def add_global_event(self, event):
        """添加世界事件"""
        self.global_events.append({
            "time": self.time,
            "event": event
        })
