
_FALLBACK_PROFILE = {'prodId': '21RM', 'deviceModel': 'SHEP-SL0-DNPro', 'deviceTypeId': '04B', 'deviceTypeName': '智能门锁', 'deviceTypeNameEn': 'Smart Lock', 'deviceName': '华为智选 德施曼智能门锁Pro', 'deviceNameEn': 'DESSMANN Smart Lock Pro（Works With HUAWEI HiLink）', 'deviceNameSpreading': '华为智选 德施曼智能门锁Pro', 'deviceNameSpreadingEn': 'DESSMANN Smart Lock Pro（Works With HUAWEI HiLink）', 'manufacturerId': '508', 'manufacturerName': '德施曼', 'manufacturerNameEn': 'DESSMANN', 'ManufacturerFullName': '德施曼机电(中国)有限公司', 'ManufacturerFullNameEn': '', 'protocolType': 'WiFi', 'uiType': 'H5', 'allowToDetail': 1, 'supportOfflineControl': 1, 'offeringCode': 'OFFE00314338', 'uriInfo': {'uri': '21RM/h5_001/index.html'}, 'authInfo': {'appId': '104539447', 'scope': ['https://www.huawei.com/auth/smarthome/opencloud']}, 'services': [{'serviceId': 'lockState', 'serviceType': 'lockState', 'characteristics': [{'characteristicName': 'state', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '休眠中', 'descEn': ''}, {'enumVal': 1, 'descCh': '已连接', 'descEn': ''}]}]}, {'serviceId': 'lockMode', 'serviceType': 'lockMode', 'characteristics': [{'characteristicName': 'mode', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '正常模式', 'descEn': ''}, {'enumVal': 1, 'descCh': '离家模式', 'descEn': ''}, {'enumVal': 2, 'descCh': '在家模式', 'descEn': ''}]}]}, {'serviceId': 'lockDefense', 'serviceType': 'lockDefense', 'characteristics': [{'characteristicName': 'defense', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '正常模式', 'descEn': ''}, {'enumVal': 1, 'descCh': '布防模式', 'descEn': ''}]}]}, {'serviceId': 'enableState', 'serviceType': 'enableState', 'characteristics': [{'characteristicName': 'lockAuto', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 0, 'descCh': '禁用', 'descEn': ''}, {'enumVal': 1, 'descCh': '启用', 'descEn': ''}]}, {'characteristicName': 'dualAuthen', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 0, 'descCh': '禁用', 'descEn': ''}, {'enumVal': 1, 'descCh': '启用', 'descEn': ''}]}, {'characteristicName': 'reactAuto', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 0, 'descCh': '禁用', 'descEn': ''}, {'enumVal': 1, 'descCh': '启用', 'descEn': ''}]}, {'characteristicName': 'stayDetection', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 0, 'descCh': '禁用', 'descEn': ''}, {'enumVal': 1, 'descCh': '启用', 'descEn': ''}]}, {'characteristicName': 'abductedFace', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 0, 'descCh': '禁用', 'descEn': ''}, {'enumVal': 1, 'descCh': '启用', 'descEn': ''}]}, {'characteristicName': 'time', 'characteristicType': 'string', 'maxLength': 32, 'method': 'RW'}, {'characteristicName': 'lockTime', 'characteristicType': 'int', 'method': 'RW', 'min': 0, 'max': 100}, {'characteristicName': 'result', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '失败', 'descEn': ''}, {'enumVal': 1, 'descCh': '成功', 'descEn': ''}]}]}, {'serviceId': 'upgradeMode', 'serviceType': 'upgradeMode', 'characteristics': [{'characteristicName': 'mode', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '非升级模式', 'descEn': ''}, {'enumVal': 1, 'descCh': '升级模式', 'descEn': ''}]}]}, {'serviceId': 'heartbeatTime', 'serviceType': 'heartbeatTime', 'characteristics': [{'characteristicName': 'time', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 100}]}, {'serviceId': 'lastActionTime', 'serviceType': 'lastActionTime', 'characteristics': [{'characteristicName': 'time', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}]}, {'serviceId': 'battery', 'serviceType': 'battery', 'characteristics': [{'characteristicName': 'level', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 100}]}, {'serviceId': 'lockAlarm', 'serviceType': 'lockAlarm', 'characteristics': [{'characteristicName': 'alarm', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '低电量告警', 'descEn': ''}, {'enumVal': 2, 'descCh': '撬锁告警', 'descEn': ''}, {'enumVal': 3, 'descCh': '指纹错误告警', 'descEn': ''}, {'enumVal': 4, 'descCh': '密码错误告警', 'descEn': ''}, {'enumVal': 5, 'descCh': '人脸错误告警', 'descEn': ''}, {'enumVal': 6, 'descCh': '指纹挟持告警', 'descEn': ''}, {'enumVal': 7, 'descCh': '密码挟持告警', 'descEn': ''}, {'enumVal': 8, 'descCh': '人脸挟持告警', 'descEn': ''}, {'enumVal': 9, 'descCh': '逗留告警', 'descEn': ''}, {'enumVal': 10, 'descCh': '布防告警', 'descEn': ''}]}, {'characteristicName': 'id', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 999}, {'characteristicName': 'alarmTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}]}, {'serviceId': 'event', 'serviceType': 'event', 'characteristics': [{'characteristicName': 'event', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '指纹开锁', 'descEn': ''}, {'enumVal': 2, 'descCh': '密码开锁', 'descEn': ''}, {'enumVal': 3, 'descCh': '人脸开锁', 'descEn': ''}, {'enumVal': 4, 'descCh': '临时密码开锁', 'descEn': ''}, {'enumVal': 5, 'descCh': '双重认证开锁', 'descEn': ''}]}, {'characteristicName': 'id', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 999}, {'characteristicName': 'eventTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}]}, {'serviceId': 'keyList', 'serviceType': 'keyList', 'characteristics': [{'characteristicName': 'list', 'characteristicType': 'object', 'max': 100, 'method': 'R', 'properties': [{'characteristicName': 'id', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 999}, {'characteristicName': 'type', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '指纹', 'descEn': ''}, {'enumVal': 2, 'descCh': '密码', 'descEn': ''}, {'enumVal': 3, 'descCh': '人脸', 'descEn': ''}]}, {'characteristicName': 'level', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '管理', 'descEn': ''}, {'enumVal': 2, 'descCh': '普通', 'descEn': ''}, {'enumVal': 3, 'descCh': '客人', 'descEn': ''}]}, {'characteristicName': 'abducted', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '非挟持', 'descEn': ''}, {'enumVal': 1, 'descCh': '挟持', 'descEn': ''}]}, {'characteristicName': 'startTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}, {'characteristicName': 'endTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}, {'characteristicName': 'repeat', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}]}]}, {'serviceId': 'keyOperate', 'serviceType': 'keyOperate', 'characteristics': [{'characteristicName': 'keyOperate', 'characteristicType': 'object', 'max': 100, 'method': 'RW', 'properties': [{'characteristicName': 'action', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '添加', 'descEn': ''}, {'enumVal': 2, 'descCh': '删除', 'descEn': ''}, {'enumVal': 3, 'descCh': '修改', 'descEn': ''}]}, {'characteristicName': 'type', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 1, 'descCh': '指纹', 'descEn': ''}, {'enumVal': 2, 'descCh': '密码', 'descEn': ''}, {'enumVal': 3, 'descCh': '人脸', 'descEn': ''}]}, {'characteristicName': 'level', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 1, 'descCh': '管理', 'descEn': ''}, {'enumVal': 2, 'descCh': '普通', 'descEn': ''}, {'enumVal': 3, 'descCh': '客人', 'descEn': ''}]}, {'characteristicName': 'abducted', 'characteristicType': 'int', 'method': 'RW', 'enumList': [{'enumVal': 0, 'descCh': '非挟持', 'descEn': ''}, {'enumVal': 1, 'descCh': '挟持', 'descEn': ''}]}, {'characteristicName': 'startTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'RW'}, {'characteristicName': 'endTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'RW'}, {'characteristicName': 'repeat', 'characteristicType': 'string', 'maxLength': 32, 'method': 'RW'}, {'characteristicName': 'result', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '取消', 'descEn': ''}, {'enumVal': 2, 'descCh': '录入成功', 'descEn': ''}, {'enumVal': 3, 'descCh': '录入失败', 'descEn': ''}, {'enumVal': 4, 'descCh': '删除成功', 'descEn': ''}, {'enumVal': 5, 'descCh': '删除失败', 'descEn': ''}, {'enumVal': 6, 'descCh': '修改成功', 'descEn': ''}, {'enumVal': 7, 'descCh': '修改失败', 'descEn': ''}, {'enumVal': 8, 'descCh': '已达上限', 'descEn': ''}]}, {'characteristicName': 'id', 'characteristicType': 'int', 'method': 'RW', 'min': 0, 'max': 999}]}]}, {'serviceId': 'publicKey', 'serviceType': 'publicKey', 'characteristics': [{'characteristicName': 'publicKey', 'characteristicType': 'string', 'maxLength': 400, 'method': 'R'}]}, {'serviceId': 'remoteCode', 'serviceType': 'remoteCode', 'characteristics': [{'characteristicName': 'cipherText', 'characteristicType': 'string', 'maxLength': 400, 'method': 'W'}, {'characteristicName': 'id', 'characteristicType': 'int', 'method': 'W', 'min': 0, 'max': 999}]}, {'serviceId': 'remoteResult', 'serviceType': 'remoteResult', 'characteristics': [{'characteristicName': 'id', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 999}, {'characteristicName': 'result', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 1, 'descCh': '临时密码创建成功', 'descEn': ''}, {'enumVal': 2, 'descCh': '临时密码创建失败', 'descEn': ''}, {'enumVal': 3, 'descCh': '临时密码删除成功', 'descEn': ''}, {'enumVal': 4, 'descCh': '临时密码删除失败', 'descEn': ''}, {'enumVal': 5, 'descCh': '管理员密码错误，临时密码创建失败', 'descEn': ''}, {'enumVal': 6, 'descCh': '管理员密码错误，临时密码删除失败', 'descEn': ''}, {'enumVal': 7, 'descCh': '命令格式错误', 'descEn': ''}, {'enumVal': 8, 'descCh': '数据解密失败', 'descEn': ''}]}]}, {'serviceId': 'remoteInfo', 'serviceType': 'remoteCode', 'characteristics': [{'characteristicName': 'id', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 999}, {'characteristicName': 'counter', 'characteristicType': 'int', 'method': 'R', 'min': 0, 'max': 15}, {'characteristicName': 'startTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}, {'characteristicName': 'endTime', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}]}, {'serviceId': 'remoteEnable', 'serviceType': 'remoteEnable', 'characteristics': [{'characteristicName': 'disabled', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '开启', 'descEn': ''}, {'enumVal': 1, 'descCh': '禁用', 'descEn': ''}]}]}, {'serviceId': 'faultCode', 'descCh': '错误和故障服务', 'characteristics': [{'characteristicName': 'code', 'characteristicType': 'int', 'method': 'R', 'enumList': [{'enumVal': 0, 'descCh': '正常', 'descEn': ''}, {'enumVal': 1, 'descCh': '欠压故障', 'descEn': ''}, {'enumVal': 2, 'descCh': '指纹头故障', 'descEn': ''}, {'enumVal': 3, 'descCh': '触屏故障', 'descEn': ''}, {'enumVal': 4, 'descCh': '时钟故障', 'descEn': ''}, {'enumVal': 5, 'descCh': '人脸模组故障', 'descEn': ''}]}, {'characteristicName': 'phone', 'characteristicType': 'string', 'method': 'R', 'enumList': [{'enumVal': '1', 'descCh': '请联系客服，电话：XXX-XXX-XXXX', 'descEn': ''}]}]}, {'serviceId': 'update', 'serviceType': 'devOta', 'characteristics': [{'characteristicName': 'action', 'characteristicType': 'enum', 'method': 'RW', 'enumList': [{'enumVal': '0', 'descCh': '检查新版本', 'descEn': ''}, {'enumVal': '1', 'descCh': '启动升级', 'descEn': ''}]}, {'characteristicName': 'version', 'characteristicType': 'string', 'maxLength': 64, 'method': 'R'}, {'characteristicName': 'introduction', 'characteristicType': 'string', 'maxLength': 1024, 'method': 'R'}, {'characteristicName': 'progress', 'characteristicType': 'int', 'min': 0, 'max': 100, 'method': 'R'}, {'characteristicName': 'bootTime', 'characteristicType': 'int', 'method': 'R'}]}, {'serviceId': 'netInfo', 'serviceType': 'netInfo', 'characteristics': [{'characteristicName': 'intensity', 'characteristicType': 'int', 'min': 0, 'max': 100, 'method': 'R'}, {'characteristicName': 'RSSI', 'characteristicType': 'int', 'method': 'R'}, {'characteristicName': 'SSID', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}, {'characteristicName': 'BSSID', 'characteristicType': 'string', 'maxLength': 32, 'method': 'R'}, {'characteristicName': 'IP', 'characteristicType': 'string', 'maxLength': 15, 'method': 'R'}]}], 'quickmenu': [{'offlineInfo': {'text': '休眠中'}, 'content': [{'text': '{lockState/state%E}'}]}]}
"""User-contributed protocol for Huawei product 21RM (华为智选 德施曼智能门锁Pro).

设备型号: SHEP-SL0-DNPro (prodId: 21RM, deviceTypeId: 04B)
制造商: 德施曼 (DESSMANN)
Profile: https://smarthome-drcn.dbankcdn.com/device/guide/21RM/21RM.json

本适配器暴露:
   1.  sensor         电池电量 (level, %)
   2.  binary_sensor  低电量告警 (device_class: battery)
   3.  binary_sensor  撬锁告警 (device_class: tamper)
   4.  sensor         门锁告警 (alarm 文本状态)
   5.  sensor         门锁模式 (正常 / 离家 / 在家)
   6.  binary_sensor  布防状态 (正常 / 布防模式)
   7.  sensor         最近开锁方式 (指纹 / 密码 / 人脸 / 临时密码 / 双重认证)
   8.  sensor         最近动作时间
   9.  sensor         故障诊断 (正常 / 欠压 / 指纹头故障 / 人脸模组等)
   10. binary_sensor  在线连接 (休眠中 / 已连接)
   11. switch         自动上锁开关 (enableState.lockAuto)
   12. switch         逗留侦测开关 (enableState.stayDetection)
   13. sensor         Wi-Fi信号强度 (netInfo.intensity, %)
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .api import EntitySpec
from .context import DeviceContext

# ---- 枚举定义 ------------------------------------------------------------

_LOCK_MODES = {
    0: "正常模式",
    1: "离家模式",
    2: "在家模式",
}

_LOCK_ALARMS = {
    1: "低电量告警",
    2: "撬锁告警",
    3: "指纹错误告警",
    4: "密码错误告警",
    5: "人脸错误告警",
    6: "指纹挟持告警",
    7: "密码挟持告警",
    8: "人脸挟持告警",
    9: "逗留告警",
    10: "布防告警",
}

_UNLOCK_EVENTS = {
    1: "指纹开锁",
    2: "密码开锁",
    3: "人脸开锁",
    4: "临时密码开锁",
    5: "双重认证开锁",
}

_FAULT_CODES = {
    0: "正常",
    1: "欠压故障",
    2: "指纹头故障",
    3: "触屏故障",
    4: "时钟故障",
    5: "人脸模组故障",
}


# ---- 工具函数 ------------------------------------------------------------

def _as_int(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, str):
        try:
            return int(round(float(value.strip())))
        except (TypeError, ValueError):
            return None
    try:
        return int(round(float(value)))
    except (TypeError, ValueError):
        return None


def _as_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        if value.casefold() in {"1", "true", "on"}:
            return True
        if value.casefold() in {"0", "false", "off"}:
            return False
    if isinstance(value, (int, float)):
        return bool(value)
    return None


# ---- 适配器类 ------------------------------------------------------------

class Product21RMAdapter:
    """华为智选 德施曼智能门锁Pro (21RM) 适配器。"""

    prod_id = "21RM"

    def entities(self, context: DeviceContext) -> tuple[EntitySpec, ...]:
        if getattr(context, "profile", None) is None:
            try:
                object.__setattr__(context, "profile", _FALLBACK_PROFILE)
            except Exception:
                pass
        specs: list[EntitySpec] = []

        # 1. 电池电量 (sensor)
        if context.has_service("battery"):
            def battery_state(device: DeviceContext) -> Mapping[str, Any]:
                val = _as_int(device.value("battery", "level"))
                return {"native_value": val if val is not None and 0 <= val <= 100 else None}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="battery",
                    name="电池电量",
                    state=battery_state,
                    metadata={
                        "device_class": "battery",
                        "unit": "%",
                        "state_class": "measurement",
                    },
                )
            )

        # 2. 门锁告警与异常 (sensor & binary_sensor)
        if context.has_service("lockAlarm"):
            def alarm_state(device: DeviceContext) -> Mapping[str, Any]:
                code = _as_int(device.value("lockAlarm", "alarm"))
                return {"native_value": _LOCK_ALARMS.get(code, "正常" if code == 0 else f"告警({code})")}

            def tamper_state(device: DeviceContext) -> Mapping[str, Any]:
                code = _as_int(device.value("lockAlarm", "alarm"))
                return {"is_on": code == 2}

            def low_batt_state(device: DeviceContext) -> Mapping[str, Any]:
                alarm_code = _as_int(device.value("lockAlarm", "alarm"))
                batt_level = _as_int(device.value("battery", "level"))
                is_low = (alarm_code == 1) or (batt_level is not None and batt_level < 20)
                return {"is_on": is_low}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="alarm",
                    name="门锁告警",
                    state=alarm_state,
                    metadata={"icon": "mdi:shield-alert"},
                )
            )
            specs.append(
                EntitySpec(
                    platform="binary_sensor",
                    key="tamper",
                    name="防撬告警",
                    state=tamper_state,
                    metadata={"device_class": "tamper"},
                )
            )
            specs.append(
                EntitySpec(
                    platform="binary_sensor",
                    key="low_battery",
                    name="低电量提醒",
                    state=low_batt_state,
                    metadata={"device_class": "battery"},
                )
            )

        # 3. 门锁模式与布防 (sensor & binary_sensor)
        if context.has_service("lockMode"):
            def mode_state(device: DeviceContext) -> Mapping[str, Any]:
                mode = _as_int(device.value("lockMode", "mode"))
                return {"native_value": _LOCK_MODES.get(mode, "正常模式")}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="lock_mode",
                    name="门锁模式",
                    state=mode_state,
                    metadata={"icon": "mdi:home-account"},
                )
            )

        if context.has_service("lockDefense"):
            def defense_state(device: DeviceContext) -> Mapping[str, Any]:
                defense = _as_int(device.value("lockDefense", "defense"))
                return {"is_on": defense == 1}

            specs.append(
                EntitySpec(
                    platform="binary_sensor",
                    key="defense",
                    name="布防状态",
                    state=defense_state,
                    metadata={"device_class": "safety"},
                )
            )

        # 4. 开锁事件与最近动作 (sensor)
        if context.has_service("event"):
            def unlock_event_state(device: DeviceContext) -> Mapping[str, Any]:
                evt = _as_int(device.value("event", "event"))
                return {"native_value": _UNLOCK_EVENTS.get(evt, "未知" if evt is not None else None)}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="last_unlock",
                    name="最近开锁方式",
                    state=unlock_event_state,
                    metadata={"icon": "mdi:lock-open-check"},
                )
            )

        if context.has_service("lastActionTime"):
            def last_action_state(device: DeviceContext) -> Mapping[str, Any]:
                time_str = device.value("lastActionTime", "time")
                return {"native_value": str(time_str) if time_str else None}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="last_action_time",
                    name="最近动作时间",
                    state=last_action_state,
                    metadata={"icon": "mdi:clock-check-outline"},
                )
            )

        # 5. 故障诊断 (sensor)
        if context.has_service("faultCode"):
            def fault_state(device: DeviceContext) -> Mapping[str, Any]:
                code = _as_int(device.value("faultCode", "code"))
                return {"native_value": _FAULT_CODES.get(code, "正常" if code is None else f"未知代码({code})")}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="fault",
                    name="故障诊断",
                    state=fault_state,
                    metadata={"icon": "mdi:alert-circle"},
                )
            )

        # 6. 在线连接状态 (binary_sensor)
        if context.has_service("lockState"):
            def connected_state(device: DeviceContext) -> Mapping[str, Any]:
                state = _as_int(device.value("lockState", "state"))
                return {"is_on": state == 1}

            specs.append(
                EntitySpec(
                    platform="binary_sensor",
                    key="connected",
                    name="连接状态",
                    state=connected_state,
                    metadata={"device_class": "connectivity"},
                )
            )

        # 7. 控制开关: 自动上锁 & 逗留侦测 (switch)
        if context.has_service("enableState"):
            def auto_lock_state(device: DeviceContext) -> Mapping[str, Any]:
                return {"is_on": _as_bool(device.value("enableState", "lockAuto"))}

            async def set_auto_lock_on(device: DeviceContext, _data: Mapping[str, Any]) -> None:
                await device.async_send_service("enableState", {"lockAuto": 1})

            async def set_auto_lock_off(device: DeviceContext, _data: Mapping[str, Any]) -> None:
                await device.async_send_service("enableState", {"lockAuto": 0})

            def stay_state(device: DeviceContext) -> Mapping[str, Any]:
                return {"is_on": _as_bool(device.value("enableState", "stayDetection"))}

            async def set_stay_on(device: DeviceContext, _data: Mapping[str, Any]) -> None:
                await device.async_send_service("enableState", {"stayDetection": 1})

            async def set_stay_off(device: DeviceContext, _data: Mapping[str, Any]) -> None:
                await device.async_send_service("enableState", {"stayDetection": 0})

            specs.append(
                EntitySpec(
                    platform="switch",
                    key="auto_lock",
                    name="自动上锁",
                    state=auto_lock_state,
                    actions={"turn_on": set_auto_lock_on, "turn_off": set_auto_lock_off},
                    metadata={"icon": "mdi:lock-clock"},
                )
            )
            specs.append(
                EntitySpec(
                    platform="switch",
                    key="stay_detection",
                    name="逗留侦测",
                    state=stay_state,
                    actions={"turn_on": set_stay_on, "turn_off": set_stay_off},
                    metadata={"icon": "mdi:motion-sensor"},
                )
            )

        # 8. Wi-Fi 信号 (sensor)
        if context.has_service("netInfo"):
            def wifi_state(device: DeviceContext) -> Mapping[str, Any]:
                intensity = _as_int(device.value("netInfo", "intensity"))
                return {"native_value": intensity if intensity is not None and 0 <= intensity <= 100 else None}

            specs.append(
                EntitySpec(
                    platform="sensor",
                    key="wifi_signal",
                    name="Wi-Fi信号强度",
                    state=wifi_state,
                    metadata={
                        "unit": "%",
                        "state_class": "measurement",
                        "icon": "mdi:wifi",
                    },
                )
            )

        return tuple(specs)


ADAPTER = Product21RMAdapter()
