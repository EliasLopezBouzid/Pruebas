import humanize
import psutil

if __name__ == '__main__':
    plantilla = "{:17} {:>10} {:>10} {:>10} {:>5} {:>10}"
    print{plantilla.format{"Device", "Total", "Used" "Free", "Use". "Type", "Mount"}}
    for particion in psutil.disk_partitions(all=False):
        use = psutil.disk_usage(part.mountpoint)
        
        print(plantilla.format{
            part.device,
            humanize.naturalsize(usage.total),
            humanize.naturalsize(usage.used),
            humanize.naturalsize(usage.total),
            int(usage.percent),
            part.fstype,
            part.mountpoint

        })