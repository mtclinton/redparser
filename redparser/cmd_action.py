from .highlight import *
from .mmap_parser import *
from .memory_parser import  *

def cmd_action(file_object, args, mmap_possible):
    try:
        if args.first:
            if args.timestamps:
                if args.ipv4 and args.ipv6:
                    if mmap_possible:
                        print(highlight_both(first(file_object, args.first, timestamp, ipv4_ipv6_all)))
                    else:
                        print(highlight_both(memory_first(file_object, args.first, timestamp, ipv4_ipv6_all)))
                elif args.ipv4:
                    if mmap_possible:
                        print(highlighter_ipv4(first(file_object, args.first, timestamp, ipv4)))
                    else:
                        print(highlighter_ipv4(memory_first(file_object, args.first, timestamp, ipv4)))
                elif args.ipv6:
                    if mmap_possible:
                        print(highlighter_ipv6(first(file_object, args.first, timestamp, ipv6)))
                    else:
                        print(highlighter_ipv6(memory_first(file_object, args.first, timestamp, ipv6)))
                else:
                    if mmap_possible:
                        print(first(file_object, args.first, timestamp))
                    else:
                        print(memory_first(file_object, args.first, timestamp))
            elif args.ipv4 and args.ipv6:
                if mmap_possible:
                    print(highlight_both(first(file_object, args.first, ipv4_ipv6_all)))
                else:
                    print(highlight_both(memory_first(file_object, args.first, ipv4_ipv6_all)))
            elif args.ipv4:
                if mmap_possible:
                    print(highlighter_ipv4(first(file_object, args.first, ipv4)))
                else:
                    print(highlighter_ipv4(memory_first(file_object, args.first, ipv4)))
            elif args.ipv6:
                if mmap_possible:
                    print(highlighter_ipv6(first(file_object, args.first, ipv6)))
                else:
                    print(highlighter_ipv6(memory_first(file_object, args.first, ipv6)))

            else:
                if mmap_possible:
                    print(first(file_object, args.first))
                else:
                    print(memory_first(file_object, args.first))

        elif args.last:
            if args.timestamps:
                if args.ipv4 and args.ipv6:
                    if mmap_possible:
                        print(highlight_both(last(file_object, args.last, timestamp, ipv4_ipv6_all)))
                    else:
                        print(highlight_both(memory_last(file_object, args.last, timestamp, ipv4_ipv6_all)))
                elif args.ipv4:
                    if mmap_possible:
                        print(highlighter_ipv4(last(file_object, args.last, timestamp, ipv4)))
                    else:
                        print(highlighter_ipv4(memory_last(file_object, args.last, timestamp, ipv4)))
                elif args.ipv6:
                    if mmap_possible:
                        print(highlighter_ipv6(last(file_object, args.last, timestamp, ipv6)))
                    else:
                        print(highlighter_ipv6(memory_last(file_object, args.last, timestamp, ipv6)))
                else:
                    if mmap_possible:
                        print(last(file_object, args.last, timestamp))
                    else:
                        print(memory_last(file_object, args.last, timestamp))
            elif args.ipv4 and args.ipv6:
                if mmap_possible:
                    print(highlight_both(last(file_object, args.last, ipv4_ipv6_all)))
                else:
                    print(highlight_both(memory_last(file_object, args.last, ipv4_ipv6_all)))
            elif args.ipv4:
                if mmap_possible:
                    print(highlighter_ipv4(last(file_object, args.last, ipv4)))
                else:
                    print(highlighter_ipv4(memory_last(file_object, args.last, ipv4)))
            elif args.ipv6:
                if mmap_possible:
                    print(highlighter_ipv6(last(file_object, args.last, ipv6)))
                else:
                    print(highlighter_ipv6(memory_last(file_object, args.last, ipv6)))

            else:
                if mmap_possible:
                    print(last(file_object, args.last))
                else:
                    print(memory_last(file_object, args.last))

        elif args.timestamps:
            if args.ipv4 and args.ipv6:
                if mmap_possible:
                    print(first(file_object, -1, timestamp, ipv4_ipv6_all))
                else:
                    print(memory_first(file_object, -1, timestamp, ipv4_ipv6_all))
            elif args.ipv4:
                if mmap_possible:
                    print(highlighter_ipv4(first(file_object, -1, timestamp, ipv4)))
                else:
                    print(highlighter_ipv4(memory_first(file_object, -1, timestamp, ipv4)))
            elif args.ipv6:
                if mmap_possible:
                    print(highlighter_ipv6(first(file_object, -1, timestamp, ipv6)))
                else:
                    print(highlighter_ipv6(memory_first(file_object, -1, timestamp, ipv6)))
            else:
                timestamp_all(file_object)
                if mmap_possible:
                    timestamp_all(file_object)
                else:
                    memory_timestamp_all(file_object)

        elif args.ipv4:
            if args.ipv6:
                print(highlight_both(first(file_object, -1, ipv4_ipv6_all)))
                if mmap_possible:
                    print(highlight_both(first(file_object, -1, ipv4_ipv6_all)))
                else:
                    print(highlight_both(memory_first(file_object, -1, ipv4_ipv6_all)))
            else:
                if mmap_possible:
                    print(highlighter_ipv4(ipv4_all(file_object)))
                else:
                    print(highlighter_ipv4(memory_ipv4_all(file_object)))
        elif args.ipv6:
            print(highlighter_ipv6(ipv6_all(file_object)))
            if mmap_possible:
                print(highlighter_ipv6(ipv6_all(file_object)))
            else:
                print(highlighter_ipv6(memory_ipv6_all(file_object)))

        else:
            raise ValueError("Error parsing cmdline options")

    except Exception as e:
        ValueError(e)