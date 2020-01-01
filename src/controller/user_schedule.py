from src.model import UserExamSubject, Information


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

    def get_my_list_schedule(self, user_id):
        my_schedule = Information()
        datas = my_schedule.get_schedule_in_student(user_id)
        data = []
        for i in datas:
            try:
                i['day'] = i['day'].strftime('%Y-%m-%d')
            except:
                pass
            i['time_end'] = i['time_end'].strftime('%H:%M')
            i['time_start'] = i['time_start'].strftime('%H:%M')

            data.append(i)
        return {"success": True, "data": data}

    def register(self, user_id, schedule_id):
        try:
            can_schedule = Information()
            datas = can_schedule.create(user_id, schedule_id)

            return {"success": True, "message": "Thành công"}
        except Exception as e:
            print(e)
            return {"success": False, "message": "Thất bại"}

    def delete(self, user_id, schedule_id):
        try:
            can_schedule = Information()
            can_schedule.delete_register(user_id, schedule_id)
            return {"success": True, "message": "Thành công"}
        except:
            return {"success": False, "message": "Thất bại"}
