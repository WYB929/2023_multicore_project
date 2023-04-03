import os
import csv
from tqdm import tqdm

home_dir = os.system("cd /home/yibin/workspace/multicore_project/parsec-3.0")
print("cd to Parsec3.0 home directionary %d" % home_dir)

input_size = ["simsmall", "simmedium", "simlarge"]

benchmarks = ["blackscholes", "bodytrack", "canneal", "dedup", "facesim", 
              "ferret", "fluidanimate", "freqmine", "streamcluster", 
              "swaptions", "vips", "x264", "splash2x.barnes", "splash2x.cholesky",
              "splash2x.fft", "splash2x.fmm", "splash2x.lu_cb", "splash2x.lu_ncb",
              "splash2x.ocean_cp", "splash2x.ocean_ncp", "splash2x.radiosity",
              "splash2x.raytrace", "splash2x.volrend", "splash2x.water_nsquared", "splash2x.water_spatial"]
threads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def parse_data(bench, size, thread, data):
    with open("result.txt", "r") as f:
        for line in f:
            line = line.strip().split(",")
            if "cycles" in line:
                cycles = line[0]
            elif "instructions" in line:
                instructions = line[0]
                ins_per_cycle = line[5]
            elif "cache-references" in line:
                cache_references = line[0]
            elif "cache-misses" in line:
                cache_misses = line[0]
                cache_misses_percent = line[5]
            elif "branch-instructions" in line:
                branch_instructions = line[0]
            elif "branch-misses" in line:
                branch_misses = line[0]
            elif "bus-cycles" in line:
                bus_cycles = line[0]
            elif "ref-cycles" in line:
                ref_cycles = line[0]
            elif "alignment-faults" in line:
                alignment_faults = line[0]
            elif "bpf-output" in line:
                bpf_output = line[0]
            elif "cpu-clock" in line:
                cpu_clock = line[0]
            elif "cpu-migrations" in line:
                cpu_migrations = line[0]
            elif "dummy" in line:
                dummy = line[0]
            elif "emulation-faults" in line:
                emulation_faults = line[0]
            elif "major-faults" in line:
                major_faults = line[0]
            elif "minor-faults" in line:
                minor_faults = line[0]
            elif "page-faults" in line:
                page_faults = line[0]
            elif "LLC-loads" in line:
                LLC_loads = line[0]
            elif "LLC-load-misses" in line:
                LLC_load_misses = line[0]
            elif "LLC-stores" in line:
                LLC_stores = line[0]
            elif "LLC-store-misses" in line:
                LLC_store_misses = line[0]
    with open ("result_time.txt", "r") as f:
        for line in f:
            if "real" in line:
                time = line.split("m")[1].split("s")[0]
            elif "user" in line:
                user_time = line.split("m")[1].split("s")[0]
            elif "sys" in line:
                sys_time = line.split("m")[1].split("s")[0]
    LLC_misses_percent = float(LLC_load_misses) / float(LLC_loads)
    LLC_store_misses_percent = float(LLC_store_misses) / float(LLC_stores)    
    data.append([bench, size, thread, cycles, instructions, ins_per_cycle, cache_references, cache_misses, cache_misses_percent, 
                 branch_instructions, branch_misses, bus_cycles, ref_cycles, alignment_faults, bpf_output, cpu_clock, cpu_migrations, 
                 dummy, emulation_faults, major_faults, minor_faults, page_faults, LLC_loads, LLC_load_misses, LLC_misses_percent, 
                 LLC_stores, LLC_store_misses, LLC_store_misses_percent, time, user_time, sys_time])
    return data

# output a txt file to record the running time of each benchmark with perf
data = [["Benchmark", "Input Size", "Threads", "cycles", "instructions", "ins_per_cycle", "cache_references", "cache_misses", "cache_misses_percent", "branches_instructions", "branch_misses", "bus_cycles", "ref_cycles", "alignment_faults", "bpf_output", "cpu_clock", "cpu_migrations", "dummy", "emulation_faults", "major_faults", "minor_faults", "page_faults", "LLC_loads", "LLC_load_misses", "LLC_misses_percent", "LLC_stores", "LLC_store_misses", "LLC_store_misses_percent", "time", "user_time", "sys_time"]]
for i in tqdm(range(10)):
    for bench in tqdm(benchmarks):
        for size in tqdm(input_size):
            for thread in tqdm(threads):
                os.system("perf stat -e cycles,instructions,cache-references,cache-misses,branch-instructions,branch-misses,bus-cycles,ref-cycles,alignment-faults,bpf-output,cpu-clock,cpu-migrations,dummy,emulation-faults,major-faults,minor-faults,page-faults,LLC-loads,LLC-load-misses,LLC-stores,LLC-store-misses -o result.txt -x, /home/yibin/workspace/multicore_project/parsec-3.0/bin/parsecmgmt -a run -p %s -i %s -n %d > result_time.txt" % (bench, size, thread))
                data = parse_data(bench, size, thread, data)

#save data to csv file
with open("dataset.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
