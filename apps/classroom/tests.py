import pytest
from concurrent import futures

from django.test import TestCase

from apps.classroom.models import ClassRoom


@pytest.mark.django_db
class TestClassRoom(TestCase):

    def test_수강신청을_하다(self):
        # 클래스룸 생성
        classroom = ClassRoom.objects.create(name="Room 1", total_capacity=10, remaining_capacity=5)
        # 좌석 신청 테스트
        assert classroom.apply_for_seat() is True
        classroom.refresh_from_db()
        assert classroom.remaining_capacity == 4

    def test_수용인원이_모두차서_수강신청에_실패하다(self):
        # 클래스룸 생성
        classroom = ClassRoom.objects.create(name="Room 1", total_capacity=1, remaining_capacity=0)

        # 좌석 신청 테스트
        assert classroom.apply_for_seat() is False
        classroom.refresh_from_db()
        assert classroom.remaining_capacity == 0

    # def test_동시간_수용인원이_모두차서_수강신청에_실패하다(self):
    #     # 클래스룸 생성
    #     classroom = ClassRoom.objects.create(name="Room 1", total_capacity=10, remaining_capacity=5)
    #
    #     def apply_for_seat_sync(classroom):
    #         # 좌석 신청 동기 함수
    #         result = classroom.apply_for_seat()
    #         classroom.refresh_from_db()
    #         return result
    #
    #     # 동시에 좌석 신청하기
    #     with futures.ThreadPoolExecutor(max_workers=5) as executor:
    #         future_classroom = [executor.submit(apply_for_seat_sync, classroom) for _ in range(5)]
    #         results = [future.result() for future in futures.as_completed(future_classroom)]
    #
    #     classroom.refresh_from_db()
    #     # 마지막 요청은 실패해야 함
    #     assert results[:-1] == [True] * 4
    #     assert results[-1] is False
    #     assert classroom.remaining_capacity == 0

