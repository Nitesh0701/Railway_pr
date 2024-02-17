from django.db import models

# Create your models here.

from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()





class Train(models.Model):
    train_number: int
    train_name: str
    run_days: List[str]
    train_src: str
    train_dstn: str
    from_std: str
    from_sta: str
    local_train_from_sta: int
    to_sta: str
    to_std: str
    from_day: int
    to_day: int
    d_day: int
    datum_from: str
    to: str
    from_station_name: str
    to_station_name: str
    duration: str
    special_train: bool
    train_type: str
    train_date: str
    class_type: List[str]

    def __init__(self, train_number: int, train_name: str, run_days: List[str], train_src: str, train_dstn: str, from_std: str, from_sta: str, local_train_from_sta: int, to_sta: str, to_std: str, from_day: int, to_day: int, d_day: int, datum_from: str, to: str, from_station_name: str, to_station_name: str, duration: str, special_train: bool, train_type: str, train_date: str, class_type: List[str]) -> None:
        self.train_number = train_number
        self.train_name = train_name
        self.run_days = run_days
        self.train_src = train_src
        self.train_dstn = train_dstn
        self.from_std = from_std
        self.from_sta = from_sta
        self.local_train_from_sta = local_train_from_sta
        self.to_sta = to_sta
        self.to_std = to_std
        self.from_day = from_day
        self.to_day = to_day
        self.d_day = d_day
        self.datum_from = datum_from
        self.to = to
        self.from_station_name = from_station_name
        self.to_station_name = to_station_name
        self.duration = duration
        self.special_train = special_train
        self.train_type = train_type
        self.train_date = train_date
        self.class_type = class_type

    @staticmethod
    def from_dict(obj: Any) -> 'Train':
        assert isinstance(obj, dict)
        train_number = int(from_str(obj.get("train_number")))
        train_name = from_str(obj.get("train_name"))
        run_days = from_list(from_str, obj.get("run_days"))
        train_src = from_str(obj.get("train_src"))
        train_dstn = from_str(obj.get("train_dstn"))
        from_std = from_str(obj.get("from_std"))
        from_sta = from_str(obj.get("from_sta"))
        local_train_from_sta = from_int(obj.get("local_train_from_sta"))
        to_sta = from_str(obj.get("to_sta"))
        to_std = from_str(obj.get("to_std"))
        from_day = from_int(obj.get("from_day"))
        to_day = from_int(obj.get("to_day"))
        d_day = from_int(obj.get("d_day"))
        datum_from = from_str(obj.get("from"))
        to = from_str(obj.get("to"))
        from_station_name = from_str(obj.get("from_station_name"))
        to_station_name = from_str(obj.get("to_station_name"))
        duration = from_str(obj.get("duration"))
        special_train = from_bool(obj.get("special_train"))
        train_type = from_str(obj.get("train_type"))
        train_date = from_str(obj.get("train_date"))
        class_type = from_list(from_str, obj.get("class_type"))
        return Train(train_number, train_name, run_days, train_src, train_dstn, from_std, from_sta, local_train_from_sta, to_sta, to_std, from_day, to_day, d_day, datum_from, to, from_station_name, to_station_name, duration, special_train, train_type, train_date, class_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["train_number"] = from_str(str(self.train_number))
        result["train_name"] = from_str(self.train_name)
        result["run_days"] = from_list(from_str, self.run_days)
        result["train_src"] = from_str(self.train_src)
        result["train_dstn"] = from_str(self.train_dstn)
        result["from_std"] = from_str(self.from_std)
        result["from_sta"] = from_str(self.from_sta)
        result["local_train_from_sta"] = from_int(self.local_train_from_sta)
        result["to_sta"] = from_str(self.to_sta)
        result["to_std"] = from_str(self.to_std)
        result["from_day"] = from_int(self.from_day)
        result["to_day"] = from_int(self.to_day)
        result["d_day"] = from_int(self.d_day)
        result["from"] = from_str(self.datum_from)
        result["to"] = from_str(self.to)
        result["from_station_name"] = from_str(self.from_station_name)
        result["to_station_name"] = from_str(self.to_station_name)
        result["duration"] = from_str(self.duration)
        result["special_train"] = from_bool(self.special_train)
        result["train_type"] = from_str(self.train_type)
        result["train_date"] = from_str(self.train_date)
        result["class_type"] = from_list(from_str, self.class_type)
        return result


class TrainListResponse:
    status: bool
    message: str
    timestamp: int
    data: List[Train]

    def __init__(self, status: bool, message: str, timestamp: int, data: List[Train]) -> None:
        self.status = status
        self.message = message
        self.timestamp = timestamp
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        status = from_bool(obj.get("status"))
        message = from_str(obj.get("message"))
        timestamp = from_int(obj.get("timestamp"))
        data = from_list(Train.from_dict, obj.get("data"))
        return TrainListResponse(status, message, timestamp, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_bool(self.status)
        result["message"] = from_str(self.message)
        result["timestamp"] = from_int(self.timestamp)
        result["data"] = from_list(lambda x: to_class(Train, x), self.data)
        return result


def TrainListResponse_from_dict(s: Any) -> TrainListResponse:
    return TrainListResponse.from_dict(s)


def TrainListResponse_to_dict(x: TrainListResponse) -> Any:
    return to_class(TrainListResponse, x)
