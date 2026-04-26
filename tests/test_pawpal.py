from datetime import date, timedelta

from pawpal_system import Owner, Pet, ScheduleEvaluator, Scheduler, Task


def test_adding_task_to_pet_increases_task_count() -> None:
	owner = Owner(name="Jordan", email="jordan@example.com", available_time_per_day=60)
	pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
	owner.add_pet(pet)

	starting_count = len(pet.tasks)
	task = Task(name="Evening Walk", category="exercise", duration=20, priority=2, pet=pet)

	owner.add_task(task)

	assert len(pet.tasks) == starting_count + 1


def test_mark_complete_changes_task_status() -> None:
	task = Task(name="Give Medication", category="health", duration=10, priority=1)

	assert task.status == "pending"
	task.mark_complete()

	assert task.status == "completed"


def test_scheduler_returns_tasks_in_chronological_order() -> None:
	owner = Owner(name="Jordan", email="jordan@example.com", available_time_per_day=120)
	pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
	owner.add_pet(pet)

	task_late = Task(
		name="Late Walk",
		category="exercise",
		duration=20,
		priority=2,
		pet=pet,
		start_time="18:00",
	)
	task_early = Task(
		name="Breakfast",
		category="feeding",
		duration=15,
		priority=2,
		pet=pet,
		start_time="08:00",
	)
	task_middle = Task(
		name="Lunch",
		category="feeding",
		duration=15,
		priority=2,
		pet=pet,
		start_time="12:00",
	)

	owner.add_task(task_late)
	owner.add_task(task_early)
	owner.add_task(task_middle)

	schedule = Scheduler(owner).generate_schedule()

	assert [item["task"] for item in schedule] == ["Breakfast", "Lunch", "Late Walk"]


def test_marking_daily_task_complete_creates_next_day_task() -> None:
	owner = Owner(name="Jordan", email="jordan@example.com", available_time_per_day=60)
	pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
	owner.add_pet(pet)

	today = date.today()
	daily_task = Task(
		name="Daily Medication",
		category="health",
		duration=10,
		priority=1,
		pet=pet,
		recurrence="daily",
		due_date=today,
	)
	owner.add_task(daily_task)

	scheduler = Scheduler(owner)
	follow_up = scheduler.mark_task_complete(daily_task, completed_on=today)

	assert daily_task.status == "completed"
	assert follow_up is not None
	assert follow_up.name == daily_task.name
	assert follow_up.status == "pending"
	assert follow_up.due_date == today + timedelta(days=1)
	assert follow_up in owner.tasks


def test_scheduler_flags_duplicate_start_time_conflicts() -> None:
	owner = Owner(name="Jordan", email="jordan@example.com", available_time_per_day=120)
	dog = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
	cat = Pet(name="Nori", species="cat", breed="Mixed", age=2)
	owner.add_pet(dog)
	owner.add_pet(cat)

	task_one = Task(
		name="Morning Walk",
		category="exercise",
		duration=30,
		priority=1,
		pet=dog,
		start_time="09:00",
	)
	task_two = Task(
		name="Vet Check-in",
		category="health",
		duration=20,
		priority=2,
		pet=cat,
		start_time="09:00",
	)
	owner.add_task(task_one)
	owner.add_task(task_two)

	scheduler = Scheduler(owner)
	schedule = scheduler.generate_schedule()
	warnings = scheduler.get_warnings()

	assert len(schedule) == 1
	assert schedule[0]["task"] == "Morning Walk"
	assert any("conflicts with 'Morning Walk'" in warning for warning in warnings)


def test_schedule_evaluator_passes_for_clean_schedule() -> None:
	owner = Owner(name="Jordan", email="jordan@example.com", available_time_per_day=120)
	pet = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
	owner.add_pet(pet)

	task_one = Task(
		name="Breakfast",
		category="feeding",
		duration=15,
		priority=1,
		pet=pet,
		start_time="08:00",
	)
	task_two = Task(
		name="Morning Walk",
		category="exercise",
		duration=30,
		priority=2,
		pet=pet,
		start_time="09:00",
	)
	owner.add_task(task_one)
	owner.add_task(task_two)

	scheduler = Scheduler(owner)
	schedule = scheduler.generate_schedule()
	report = ScheduleEvaluator(owner).evaluate(schedule, scheduler.get_warnings())

	assert report.passed is True
	assert report.score == 100.0
	assert report.checks["within_time_budget"] is True
	assert report.checks["sorted_by_scheduler_rules"] is True
	assert report.issues == []


def test_schedule_evaluator_flags_conflicts_as_review_needed() -> None:
	owner = Owner(name="Jordan", email="jordan@example.com", available_time_per_day=120)
	dog = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
	cat = Pet(name="Nori", species="cat", breed="Mixed", age=2)
	owner.add_pet(dog)
	owner.add_pet(cat)

	task_one = Task(
		name="Morning Walk",
		category="exercise",
		duration=30,
		priority=1,
		pet=dog,
		start_time="09:00",
	)
	task_two = Task(
		name="Vet Check-in",
		category="health",
		duration=20,
		priority=2,
		pet=cat,
		start_time="09:00",
	)
	owner.add_task(task_one)
	owner.add_task(task_two)

	scheduler = Scheduler(owner)
	schedule = scheduler.generate_schedule()
	report = ScheduleEvaluator(owner).evaluate(schedule, scheduler.get_warnings())

	assert report.passed is False
	assert report.checks["no_warnings"] is False
	assert report.warnings
	assert any("conflicts with 'Morning Walk'" in warning for warning in report.warnings)
