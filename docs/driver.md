# Driver: Aiyima 4″ full-range

Le Petit is drawn for the Fostex FE103NV2; this build uses an **Aiyima 4″ full-range**, sold as
"High fidelity full range speaker" in a 4 Ω and an **8 Ω version (used here)**. The manufacturer's lab
sheets name it **RF-406pro**. Everything known about it, from three sources: the seller's listing, the
manufacturer's lab measurements, and what was measured on these two drivers.

## The seller's listing

| | |
| --- | --- |
| Impedance | 4 / 8 Ω (two versions) |
| Rated power | 25 W |
| Frequency range | 72 Hz – 20 kHz |
| Sensitivity | 91 dB ± 3 dB |
| Voice coil | Ø 25 mm, former "AKSV" |
| Cone | cotton and linen fibre + bamboo fibre |
| Vas · Qts · Bl | 9 l · 0.52 · 2.5 |
| Magnet | Ø 85 mm outside |
| Weight | 1.1 kg |
| Recommended port | Ø 36 mm inside, 120 mm long |

## The manufacturer's lab sheet (4 Ω version)

Thiele/Small parameters from the LinearX LMS notes of the RF-406pro, measured 7 May 2019 — **for
the 4 Ω version** (Revc 3.4 Ω):

| Parameter | Value | | Parameter | Value |
| --- | --- | --- | --- | --- |
| Revc | 3.40 Ω | | Fs | **72.95 Hz** |
| Bl | 2.58 T·m | | Sd | 51.5 cm² (≈ 81 mm effective Ø) |
| Qms | 8.17 | | Mms | 2.38 g (Mmd 2.17 g) |
| Qes | 0.558 | | Cms | 2.00 mm/N |
| **Qts** | **0.522** | | Vas | **7.53 l** |
| η0 | 0.51 % | | SPLo (1 W) | 89.1 dB |

- **Impedance:** two curves — free air with the peak of ≈ 52 Ω at 73 Hz, and a second run with
  added mass (resonance ≈ 48 Hz) from which Mms and Vas follow. Minimum ≈ 4 Ω around 180–200 Hz,
  rising slowly to ≈ 8.5 Ω at 20 kHz — a small voice-coil inductance.
- **Frequency response** (measured 30 April 2019): ≈ 90 dB from 100 to 400 Hz, a shallow dip to ≈ 86 dB
  around 500 Hz, then rising from 2 kHz to peaks of ≈ 96–98 dB around **5 and 6.5 kHz** and ≈ 96 dB
  near 10 kHz. Below 100 Hz it falls steadily: ≈ 82 dB at 50 Hz, ≈ 64 dB at 20 Hz.

The listing rounds these: Vas 9 l against 7.5 l measured, sensitivity 91 dB against SPLo 89.1 dB, the
lower limit 72 Hz is simply Fs.

## Measured on these drivers (8 Ω version)

| | |
| --- | --- |
| Impedance plateau | 7.6–7.9 Ω (the lab sheet describes the 4 Ω version) |
| Resonance in the box | Fs ≈ 82 Hz estimated from the impedance, on a new suspension |
| Box tuning | Fb ≈ 48 Hz with the 175 mm port ([Step 2](06-step-2-port-tube.md)) |
| Treble | two peaks remain, near 6 and 10.5 kHz — close to the lab sheet's treble peaks; EQ them to taste |
| Rating | 25 W — usable with ordinary class D amplifiers, unlike the FE103NV2's 5 W |

## What follows for the box

- **Qts ≈ 0.52 and Vas ≈ 7.5 l** make this a driver for a small bass-reflex box; Le Petit's 27 l is
  large for it. That is why the box tunes low and flat with a long port (175 mm, ≈ 48 Hz) rather than
  the seller's short Ø 36 × 120 mm port, which is meant for a much smaller cabinet.
- **The cutout:** Ø 94 mm in the front; the Ø 85 mm magnet passes through it from the front.
- **Check the impedance first** when you buy one: the 4 Ω and 8 Ω versions look identical, and the
  plateau tells them apart in a minute ([impedance jig](03-impedance-jig.md)).

How it compares with the plan's FE103NV2, and what that means for tuning:
[Aiyima vs. FE103NV2](07-aiyima-vs-fe103.md).
