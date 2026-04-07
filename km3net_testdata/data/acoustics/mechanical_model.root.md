# Mechanical Model

The ROOT file stores the mechanical model and was produced by the following
commands (in reverse order):

```
JKatoomba 20.0.0-85-gc433f94f2-D
JKatoomba 6.30/02
JKatoomba /localstore/km3net/mjg/GIT/Jpp/out//Linux/bin//JKatoomba -a detector.datx -f KM3NeT_00000148_00016662_event.root -o katoomba.root -T .//tripod.txt -V .//sound_velocity.txt -M .//mechanics.txt -@ .//acoustics_fit_parameters.txt -! .//disable.txt \"-C -JEvent\" -d 2 --!
JKatoomba KM3NET
JKatoomba Linux lbp002pyw.nikhef.nl 5.14.0-570.58.1.el9_6.x86_64 #1 SMP PREEMPT_DYNAMIC Fri Oct 31 13:55:05 UTC 2025 x86_64

JAcousticsEventBuilder 20.0.0-88-g697a5cfbc-D
JAcousticsEventBuilder 6.30/02
JAcousticsEventBuilder /localstore/km3net/mjg/GIT/Jpp.dynamics-mechanics/out//Linux/bin//JAcousticsEventBuilder -a detector.datx -f .//KM3NeT_00000148_00016662_toa.root -T .//tripod.txt -Y .//transmitter.txt -V .//sound_velocity.txt -W .//waveform.txt -@ .//acoustics_trigger_parameters.txt -H .//hydrophone.txt -o .//KM3NeT_00000148_00016662_event.root -d 2 --!
JAcousticsEventBuilder KM3NET
JAcousticsEventBuilder Linux lbp002pyw.nikhef.nl 5.14.0-570.58.1.el9_6.x86_64 #1 SMP PREEMPT_DYNAMIC Fri Oct 31 13:55:05 UTC 2025 x86_64

JToA 20.0.0-88-g697a5cfbc-D
JToA 6.30/02
JToA /localstore/km3net/mjg/GIT/Jpp.dynamics-mechanics/out//Linux/bin//JToA -@ \"detid  = D0ORCA018\" -@ \"minrun = 16662\" -@ \"maxrun = 16662\" -@ \"QUALITYFACTOR >= 2.0e3\" -o .//KM3NeT_00000148_00016662_toa.root -d 2 --!
JToA KM3NET
JToA Linux lbp002pyw.nikhef.nl 5.14.0-570.58.1.el9_6.x86_64 #1 SMP PREEMPT_DYNAMIC Fri Oct 31 13:55:05 UTC 2025 x86_64
```
