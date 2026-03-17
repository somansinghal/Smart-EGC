from database import SessionLocal, ECGRecord

def save_ecg(patient_id, heart_rate, ecg_value):

    db = SessionLocal()

    record = ECGRecord(
        patient_id=patient_id,
        heart_rate=heart_rate,
        ecg_value=ecg_value
    )

    db.add(record)
    db.commit()

    db.close()