# Advent of Code - 2025

Whats advent of code: [https://adventofcode.com/](https://adventofcode.com/)

Disclaimer: This repo shows my solutions for the Advent of Code challenges. The general coding style may vary and is usually not the level of polish I normally strive for. The main goal here is to solve the challenges, not to write perfect code that works in every edge case and fails safely.

|Day|Star 1|Used AI|Language|Runtime|Star 2|Used AI|Language|Runtime|
|---|------|-------|--------|----------------|------|-------|--------|----------------|
|1| ✅ | ❌ | 🐍 |  0.0013s | ✅ | ❌ | 🐍 | 0.0019s |
|2| ✅ | ❌ | 🐍 | 1.7s | ✅ | ❌ | 🐍 | 2.3s |
|3| ✅ | ❌ | 🐍 | 0.010s | ✅ | ❌ | 🐍 | 0.022s |
|4| ✅ | ✅ | 🐍 | 0.0007s | ✅ | ❌ | 🐍| 0.033s |
|5| ✅ | ❌ | 🐍 | 0.0015s | ✅ | ❌ | 🐍 | 0.0s |
|6| ✅ | ❌ | 🐍 | 0.0045s | ✅ | ✅ | 🐍 | 0.0013s |
|7| ✅ | ❌ | 🐍 | 0.0078s | ✅ | ❌ | 🐍 | 0.007s |
|8| ✅ | ❌ | 🐍 | 2.67s | ✅ | ❌ | 🐍 | 2.81s |
|9| ✅ | ❌ | 🐍 | 0.04s | ✅ | ✅ | 🐍 | 0.75s |
|10| ✅ | ✅ | 🐍| 0.1s | ✅ | ❌ | 🐍 | 0.23s |
|11| ✅ | ❌ | 🐍| 0.0s | ✅ | ✅ | 🐍 | 0.034s |
|12| ❔ | ❔ | ❔ | ❔ | ❔ | ❔ | ❔ | ❔ |
>Legend: ✅ - solved, ❌ - not solved, ❔ - unknown
>Note: The runtimes are measured on my local machine using the included [average_runtime.py](./average_runtime.py) script. It measures raw execution time without any writing to console or files. Furthermore, the files are imported as modules, so any library overhead (cough Numpy cough) and input parsing is not included in the measurement. However, any cache functions are disabled as they would throw off run-to-run variants. It only measures the raw execution time of the solver functions individually.