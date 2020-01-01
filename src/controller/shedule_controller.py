from sched import scheduler

from src.model import Schedule
import datetime

class ScheduleController:

    def create(self, exam_id, room_id, subject_id, day, start_time, end_time):
        print(subject_id)
        print (end_time)
        try:

            schedule = Schedule.create(exam_id=exam_id, room_id=room_id, subject_id=subject_id, day=day,
                                       time_start=start_time, time_end=end_time)
            schedule.save()
            return {"success": True, "message": "Thành công","schedule_id":schedule.id }
        except Exception as e:
            print(e)
            return {"success": False, "message": "Thất bại"}

    def update(self, id, exam_id, room_id, subject_id, day, start_time, end_time):
        try:
            schedule = Schedule.get_by_id(id)
            schedule.time_start=start_time
            schedule.time_end=end_time
            schedule.exam_id=exam_id
            schedule.room_id=room_id
            schedule.subject_id=subject_id
            schedule.day=day
            schedule.update()
            return {"success": True, "message": "Thành công", "schedule_id": schedule.id}
        except:
            return {"success": False, "message": "Thất bại"}

    def get_list(self):
        schedule = Schedule()
        datas = schedule.get_list()
        print(datas)
        data = []
        for i in datas:

            print(i)
            i['day']=i['day'].strftime('%Y-%m-%d')
            i['time_end']=i['time_end'].strftime('%H:%M')
            i['time_start'] = i['time_start'].strftime('%H:%M')
            data.append(i)
        return {"success": True, "schedules": data}

    def delete(self, id):
        try:
            schedule = Schedule.get(Schedule.id == id)
            schedule.delete()
            return {"success": True, "message": "Thành công", }
        except Exception as e:
            return {"success": False, "message": "Thất bại"}
