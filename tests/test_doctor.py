from ignite.doctor import generate_doctor_report


def test_doctor_score_with_no_issues(tmp_path):
    report = generate_doctor_report(tmp_path)

    assert report["score"] == 100


def test_doctor_score_never_below_50(monkeypatch):
    from ignite import doctor

    monkeypatch.setattr(
        doctor,
        "analyze_project",
        lambda _: {
            "detected": [],
            "configured_rules": [],
            "missing_rules": ["a", "b", "c", "d", "e", "f"],
        },
    )

    report = doctor.generate_doctor_report(None)

    assert report["score"] == 50