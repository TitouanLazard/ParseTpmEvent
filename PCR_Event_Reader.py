import sys
import struct

#See https://trustedcomputinggroup.org/wp-content/uploads/EFI-Protocol-Specification-rev13-160330final.pdf





def usage():
    print("{} <path to event log file>".format(sys.argv[0]))
    print("Usually located at /sys/kernel/security/tpm0/binary_bios_measurements")

def pretty_print(e):
    print(e)
    

def read_events_from_file(f):
    head_fix_size = 32
    with open(f, "rb") as event_f:
        d = event_f.read(head_fix_size)
        while(len(d) == head_fix_size):
            event_id = struct.unpack("II20sI",d)
            print(event_id)
            data = event_f.read(event_id[-1])
            print(data)
            d = event_f.read(head_fix_size)
            
if __name__=="__main__":
    if "-h" in sys.argv:
        usage()

    else:
        print(read_events_from_file(sys.argv[1]))
