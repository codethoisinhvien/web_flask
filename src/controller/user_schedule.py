from src.model import UserExamSubject,Information


class UserScheduleController:
    def get_list_can_schedule(self, user_id):
        can_schedule = UserExamSubject()
        datas = can_schedule.get_list_can_schedule(user_id)
        data = []
        for i in datas:
            i['day'] = i['day'].strftime('%Y-%m-%d')
            i['time_end'] = i['time_end'].strftime('%H:%M')
            i['time_start'] = i['time_start'].strftime('%H:%M')
            data.append(i)
            print(i)
        return {"success": True, "data": data}

    def get_my_list_schedule(self):
        pass

    def register(self,user_id,schedule_id):
        can_schedule = Information()
        datas =can_schedule.create(user_id,schedule_id)
        return "12213"

