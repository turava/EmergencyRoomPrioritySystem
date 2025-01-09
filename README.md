# Emergency Room Priority System

## Overview
This project implements a priority management system for an emergency room using custom Max and Min Heaps. The system prioritizes patients based on two criteria:

1. **Urgency Level**: Patients with higher urgency are attended first.
2. **Waiting Time**: If no high-urgency patients are present, patients with the longest waiting time are attended.

The system ensures efficient and fair management of patient attention in critical situations.

---

## Features

### Max Heap (Urgency Level)
- Prioritizes patients with the highest urgency (level 10 is the maximum).
- Allows O(log n) insertion and deletion operations.

### Min Heap (Waiting Time)
- Helps identify patients who have waited the longest.
- Ensures fair treatment when no high-urgency cases are present.

### Patient Management
- Automatically adds patients to both heaps.
- Attends patients based on urgency and waiting rules.
- Dynamically rebuilds heaps to maintain consistency.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/turava/EmergencyRoomPrioritySystem.git
   ```
2. Navigate to the project directory:
   ```bash
   cd emergency-room-priority-system
   ```

---

## Usage

1. Run the main script:
   ```bash
   python emergency_priority_system.py
   ```
2. The system will:
   - Generate random patients.
   - Display the current state of the emergency room.
   - Simulate attending patients based on urgency and waiting time.

---

## Project Structure

- `Paciente`: Represents a patient with:
  - **Name**: Patient's name.
  - **Urgency Level**: How critical the patient's condition is (1 to 10).
  - **Waiting Time**: How many hours the patient has been waiting.

- `Heap`: Custom implementation of a heap supporting both max-heap and min-heap operations.

- `SalaEmergencias`: Manages patients using the heaps and applies prioritization rules.

---

## Example Output

```plaintext
Agregando pacientes a la sala de emergencias...
Pacientes en la sala de emergencias:
Por urgencia (Max Heap): [Paciente(María, Urgencia: 10, Espera: 1h), Paciente(Luis, Urgencia: 5, Espera: 2h), ...]
Por tiempo de espera (Min Heap): [Paciente(Carlos, Urgencia: 4, Espera: 6h), Paciente(Ana, Urgencia: 6, Espera: 4h), ...]

Simulando atención de pacientes...
Atendiendo al paciente con máxima urgencia: Paciente(María, Urgencia: 10, Espera: 1h)
Atendiendo al paciente que ha esperado más de 5 horas: Paciente(Carlos, Urgencia: 4, Espera: 6h)
```

---

## Tests

1. Run the unit tests:
   ```bash
   python -m unittest test_emergency_priority_system.py
   ```
2. The tests will validate:
   - Adding patients to the system.
   - Proper prioritization and attendance.
   - Consistent heap management.

---

## Contributions

Feel free to submit issues and pull requests! Contributions are welcome to improve functionality, performance, or add new features.

---

## License

This project is licensed under the [MIT License](LICENSE).
