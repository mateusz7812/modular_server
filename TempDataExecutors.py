import json

import redis

from SessionManager import SessionExecutorBase


class RedisExecutor(SessionExecutorBase):
    def __init__(self):
        super().__init__()
        self.password = self.get_pass()

        self.redis = redis.Redis(
            host='localhost',
            port='6379',
            password=self.password
        )

    def get_pass(self):
        import os
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        with open(cur_dir + "\\pass\\rpass") as f:
            data = f.readline()
        return data

    def add(self, data):
        self.redis.set(data[0], data[1])
        return True

    def get(self, data):
        return data[1] == self.redis.get(data[0])

    def delete(self, data):
        if self.redis.get(data[0]) == data[1]:
            self.redis.delete(data[0])
            return True
        return False


class TextTempExecutor(SessionExecutorBase):
    import os
    cur_dir = os.path.dirname(os.path.abspath(__file__))

    def add(self, data):
        row = json.dumps(data)
        with open(self.cur_dir + "\\textDataBases\\temp", "a") as f:
            f.write(row + "\n")
        return True

    def get(self, data):
        row = json.dumps(data) + "\n"
        with open(self.cur_dir + "\\textDataBases\\temp", "r") as f:
            all_rows = f.readlines()
        return row in all_rows

    def delete(self, data):
        row = json.dumps(data) + "\n"
        if self.get(data):
            with open(self.cur_dir + "\\textDataBases\\temp", "r") as f:
                all_rows = f.readlines()
            all_rows.remove(row)
            with open(self.cur_dir + "\\textDataBases\\temp", "w") as f:
                f.writelines(all_rows)
            return True
        return False
