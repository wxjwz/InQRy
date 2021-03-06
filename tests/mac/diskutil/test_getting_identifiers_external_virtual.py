from inqry.system_specs import diskutil

DISKUTIL_LIST_OUTPUT = '''
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:          Apple_CoreStorage Machintosh HD           999.7 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3

/dev/disk1 (internal, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                            Macintosh HD           +999.3 GB   disk1
                                 Logical Volume on disk0s2
                                 05F5DF37-4C54-4810-82CE-9BF556A85116
                                 Unlocked Encrypted

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk2
   1:                        EFI EFI                     209.7 MB   disk2s1
   2:                 Apple_RAID                         999.9 GB   disk2s2
   3:                 Apple_Boot Boot OS X               134.2 MB   disk2s3

/dev/disk3 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk3
   1:                        EFI EFI                     209.7 MB   disk3s1
   2:                 Apple_RAID                         999.9 GB   disk3s2
   3:                 Apple_Boot Boot OS X               134.2 MB   disk3s3

/dev/disk4 (external, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS Builds                 +2.0 TB     disk4
'''


def test_all_physical_disk_identifiers():
    expected_disk_ids = ['/dev/disk0', '/dev/disk1', '/dev/disk2', '/dev/disk3', '/dev/disk4']
    assert expected_disk_ids == diskutil.get_all_physical_ids(DISKUTIL_LIST_OUTPUT)
