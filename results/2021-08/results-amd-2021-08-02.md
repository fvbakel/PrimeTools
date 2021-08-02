# Prime results

Report date in UTC: 2021-08-02 16:47:17

1. [Top 10 single threaded](#top-10-single-threaded)
2. [Top 10 multi threaded](#top-10-multi-threaded)
3. [All results](#all-results)
4. [Test details](#test-details)

### Base, Faithful, 1 thread, 1 bit

|    | implementation   |   solution | label                                        |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:---------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | rust             |          1 | mike-barber_bit-storage-striped              |         1832.71  |     9164 |    5.00024 |         1 | base        | yes        |      1 |        nan |
|  2 | rust             |          1 | mike-barber_bit-storage-striped-blocks       |         1612.39  |     8063 |    5.00066 |         1 | base        | yes        |      1 |        nan |
|  3 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small |         1442.08  |     7211 |    5.00042 |         1 | base        | yes        |      1 |        nan |
|  4 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc |          839.007 |     4196 |    5.00115 |         1 | base        | yes        |      1 |        nan |
|  5 | cython           |          1 | rpkak+bit-array                              |          739.641 |     3699 |    5.00108 |         1 | base        | yes        |      1 |        nan |
|  6 | fortran          |          2 | tjol-bits                                    |          733.804 |     3670 |    5.00134 |         1 | base        | yes        |      1 |        nan |
|  7 | rust             |          1 | mike-barber_bit-storage                      |          673.009 |     3366 |    5.00142 |         1 | base        | yes        |      1 |        nan |
|  8 | rust             |          1 | mike-barber_bit-storage-rotate               |          648.988 |     3245 |    5.00009 |         1 | base        | yes        |      1 |        nan |
|  9 | odin             |          1 | odin_bit_moe                                 |          625.4   |     3127 |    5       |         1 | base        | yes        |      1 |        nan |
| 10 | c                |          2 | danielspaangberg_1of2                        |          586.797 |     2934 |    5.00003 |         1 | base        | yes        |      1 |        nan |
### Not wheel, Faithful, 1 thread

|    | implementation   |   solution | label                                        |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:---------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | c                |          3 | fvbakel_Cwords                               |         1916.93  |     9585 |    5.00018 |         1 | other       | yes        |      1 |        nan |
|  2 | rust             |          1 | mike-barber_bit-storage-striped              |         1832.71  |     9164 |    5.00024 |         1 | base        | yes        |      1 |        nan |
|  3 | rust             |          1 | mike-barber_bit-storage-striped-blocks       |         1612.39  |     8063 |    5.00066 |         1 | base        | yes        |      1 |        nan |
|  4 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small |         1442.08  |     7211 |    5.00042 |         1 | base        | yes        |      1 |        nan |
|  5 | cython           |          1 | ssovest-cy                                   |         1400.16  |     7001 |    5.00014 |         1 | other       | yes        |      1 |        nan |
|  6 | go               |          2 | ssovest-go-other-B                           |         1195.88  |     5980 |    5.0005  |         1 | other       | yes        |      1 |        nan |
|  7 | go               |          2 | ssovest-go-other                             |         1109.89  |     5551 |    5.00138 |         1 | other       | yes        |      1 |        nan |
|  8 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc |          839.007 |     4196 |    5.00115 |         1 | base        | yes        |      1 |        nan |
|  9 | cython           |          1 | rpkak+bit-array                              |          739.641 |     3699 |    5.00108 |         1 | base        | yes        |      1 |        nan |
| 10 | fortran          |          2 | tjol-bits                                    |          733.804 |     3670 |    5.00134 |         1 | base        | yes        |      1 |        nan |
### Faithful, 1 thread

|    | implementation   |   solution | label                                        |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:---------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | rust             |          1 | mike-barber_bit-storage-striped              |         1832.71  |     9164 |    5.00024 |         1 | base        | yes        |      1 |        nan |
|  2 | rust             |          1 | mike-barber_bit-storage-striped-blocks       |         1612.39  |     8063 |    5.00066 |         1 | base        | yes        |      1 |        nan |
|  3 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small |         1442.08  |     7211 |    5.00042 |         1 | base        | yes        |      1 |        nan |
|  4 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc |          839.007 |     4196 |    5.00115 |         1 | base        | yes        |      1 |        nan |
|  5 | cython           |          1 | rpkak+bit-array                              |          739.641 |     3699 |    5.00108 |         1 | base        | yes        |      1 |        nan |
|  6 | fortran          |          2 | tjol-bits                                    |          733.804 |     3670 |    5.00134 |         1 | base        | yes        |      1 |        nan |
|  7 | rust             |          1 | mike-barber_bit-storage                      |          673.009 |     3366 |    5.00142 |         1 | base        | yes        |      1 |        nan |
|  8 | rust             |          1 | mike-barber_bit-storage-rotate               |          648.988 |     3245 |    5.00009 |         1 | base        | yes        |      1 |        nan |
|  9 | odin             |          1 | odin_bit_moe                                 |          625.4   |     3127 |    5       |         1 | base        | yes        |      1 |        nan |
| 10 | c                |          2 | danielspaangberg_1of2                        |          586.797 |     2934 |    5.00003 |         1 | base        | yes        |      1 |        nan |
### Single threaded

|    | implementation   |   solution | label                                           |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:------------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-clang      |         61790.4  |   308954 |    5.00003 |         1 | base        | no         |      1 |        nan |
|  2 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-gcc        |         24439.2  |   122197 |    5.00005 |         1 | base        | no         |      1 |        nan |
|  3 | cpp              |          3 | flo80_constexpr                                 |         14043.2  |    70217 |    5.00006 |         1 | base        | no         |      1 |        nan |
|  4 | rust             |          6 | SycrationSinglethreaded                         |          3123.07 |    15616 |    5.00021 |         1 | base        | no         |    nan |        nan |
|  5 | c                |          2 | danielspaangberg_5760of30030_owrb               |          1948.53 |     9743 |    5.00017 |         1 | wheel       | yes        |      1 |        nan |
|  6 | c                |          3 | fvbakel_Cwords                                  |          1916.93 |     9585 |    5.00018 |         1 | other       | yes        |      1 |        nan |
|  7 | rust             |          1 | mike-barber_bit-storage-striped                 |          1832.71 |     9164 |    5.00024 |         1 | base        | yes        |      1 |        nan |
|  8 | c                |          2 | danielspaangberg_480of2310_owrb                 |          1749.77 |     8749 |    5.0001  |         1 | wheel       | yes        |      1 |        nan |
|  9 | c                |          1 | mckoss-c830                                     |          1668.2  |     8341 |    5       |         1 | wheel       | yes        |      1 |        nan |
| 10 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_bits<u32>-clang |          1640.99 |     8205 |    5.00004 |         1 | wheel       | yes        |      1 |        nan |
## Top 10 multi threaded

### Base, Faithful, multi thread, 1 bit

|    | implementation   |   solution | label                                        |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:---------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | rust             |          1 | mike-barber_bit-storage-striped              |         3526.2   |    17633 |    5.00057 |         2 | base        | yes        |      1 |        nan |
|  2 | rust             |          1 | mike-barber_bit-storage-striped-blocks       |         3136.47  |    15684 |    5.00052 |         2 | base        | yes        |      1 |        nan |
|  3 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small |         2792.8   |    13965 |    5.00036 |         2 | base        | yes        |      1 |        nan |
|  4 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc |         1683.81  |     8421 |    5.00116 |         2 | base        | yes        |      1 |        nan |
|  5 | rust             |          1 | mike-barber_bit-storage                      |         1311.24  |     6558 |    5.00138 |         2 | base        | yes        |      1 |        nan |
|  6 | rust             |          1 | mike-barber_bit-storage-rotate               |         1261.62  |     6310 |    5.00151 |         2 | base        | yes        |      1 |        nan |
|  7 | odin             |          1 | odin_bit_threaded_moe                        |         1220.91  |     6107 |    5.002   |         2 | base        | yes        |      1 |        nan |
|  8 | c                |          2 | danielspaangberg_1of2_epar                   |         1161.8   |     5812 |    5.00257 |         2 | base        | yes        |      1 |        nan |
|  9 | cpp              |          2 | davepl_par                                   |         1069.69  |     5350 |    5.00143 |         2 | base        | yes        |      1 |        nan |
| 10 | c                |          2 | danielspaangberg_1of2_par                    |          963.395 |     4817 |    5.00003 |         2 | base        | yes        |      1 |        nan |
### Not wheel, Faithful, multi thread

|    | implementation   |   solution | label                                        |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:---------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | rust             |          1 | mike-barber_bit-storage-striped              |         3526.2   |    17633 |    5.00057 |         2 | base        | yes        |      1 |        nan |
|  2 | rust             |          1 | mike-barber_bit-storage-striped-blocks       |         3136.47  |    15684 |    5.00052 |         2 | base        | yes        |      1 |        nan |
|  3 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small |         2792.8   |    13965 |    5.00036 |         2 | base        | yes        |      1 |        nan |
|  4 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc |         1683.81  |     8421 |    5.00116 |         2 | base        | yes        |      1 |        nan |
|  5 | rust             |          1 | mike-barber_bit-storage                      |         1311.24  |     6558 |    5.00138 |         2 | base        | yes        |      1 |        nan |
|  6 | rust             |          1 | mike-barber_bit-storage-rotate               |         1261.62  |     6310 |    5.00151 |         2 | base        | yes        |      1 |        nan |
|  7 | odin             |          1 | odin_bit_threaded_moe                        |         1220.91  |     6107 |    5.002   |         2 | base        | yes        |      1 |        nan |
|  8 | c                |          2 | danielspaangberg_1of2_epar                   |         1161.8   |     5812 |    5.00257 |         2 | base        | yes        |      1 |        nan |
|  9 | cpp              |          2 | davepl_par                                   |         1069.69  |     5350 |    5.00143 |         2 | base        | yes        |      1 |        nan |
| 10 | c                |          2 | danielspaangberg_1of2_par                    |          963.395 |     4817 |    5.00003 |         2 | base        | yes        |      1 |        nan |
### Faithful, multi thread

|    | implementation   |   solution | label                                        |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:---------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | rust             |          1 | mike-barber_bit-storage-striped              |         3526.2   |    17633 |    5.00057 |         2 | base        | yes        |      1 |        nan |
|  2 | rust             |          1 | mike-barber_bit-storage-striped-blocks       |         3136.47  |    15684 |    5.00052 |         2 | base        | yes        |      1 |        nan |
|  3 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small |         2792.8   |    13965 |    5.00036 |         2 | base        | yes        |      1 |        nan |
|  4 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc |         1683.81  |     8421 |    5.00116 |         2 | base        | yes        |      1 |        nan |
|  5 | rust             |          1 | mike-barber_bit-storage                      |         1311.24  |     6558 |    5.00138 |         2 | base        | yes        |      1 |        nan |
|  6 | rust             |          1 | mike-barber_bit-storage-rotate               |         1261.62  |     6310 |    5.00151 |         2 | base        | yes        |      1 |        nan |
|  7 | odin             |          1 | odin_bit_threaded_moe                        |         1220.91  |     6107 |    5.002   |         2 | base        | yes        |      1 |        nan |
|  8 | c                |          2 | danielspaangberg_1of2_epar                   |         1161.8   |     5812 |    5.00257 |         2 | base        | yes        |      1 |        nan |
|  9 | cpp              |          2 | davepl_par                                   |         1069.69  |     5350 |    5.00143 |         2 | base        | yes        |      1 |        nan |
| 10 | c                |          2 | danielspaangberg_1of2_par                    |          963.395 |     4817 |    5.00003 |         2 | base        | yes        |      1 |        nan |
### Multi threaded

|    | implementation   |   solution | label                                             |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits |   parallel |
|---:|:-----------------|-----------:|:--------------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|-----------:|
|  1 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-clang        |        117190    |   585970 |    5.00017 |         2 | base        | no         |      1 |        nan |
|  2 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-gcc          |         58194.3  |   290975 |    5.00006 |         2 | base        | no         |      1 |        nan |
|  3 | cpp              |          3 | flo80_constexpr                                   |         16809.4  |    84048 |    5.00006 |         2 | base        | no         |      1 |        nan |
|  4 | rust             |          6 | SycrationMultithreaded                            |          4206.1  |    21095 |    5.01534 |         8 | base        | no         |    nan |        nan |
|  5 | rust             |          1 | mike-barber_bit-storage-striped                   |          3526.2  |    17633 |    5.00057 |         2 | base        | yes        |      1 |        nan |
|  6 | c                |          2 | danielspaangberg_5760of30030_epar                 |          3501.21 |    17509 |    5.00084 |         2 | wheel       | yes        |      1 |        nan |
|  7 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_bits<u32>-clang   |          3204.63 |    16024 |    5.00027 |         2 | wheel       | yes        |      1 |        nan |
|  8 | c                |          2 | danielspaangberg_480of2310_epar                   |          3143.07 |    15719 |    5.00115 |         2 | wheel       | yes        |      1 |        nan |
|  9 | rust             |          1 | mike-barber_bit-storage-striped-blocks            |          3136.47 |    15684 |    5.00052 |         2 | base        | yes        |      1 |        nan |
| 10 | cpp              |          4 | BlackMark-5760of30030-os-hs-maskedbits<u32>-clang |          3013.18 |    15076 |    5.00336 |         2 | wheel       | yes        |      1 |        nan |
## All results

|     | implementation   |   solution | label                                             |   passes per sec |   passes |   duration |   threads | algorithm   | faithful   |   bits | parallel   |
|----:|:-----------------|-----------:|:--------------------------------------------------|-----------------:|---------:|-----------:|----------:|:------------|:-----------|-------:|:-----------|
|   1 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-clang        |  117190          |   585970 |    5.00017 |         2 | base        | no         |      1 | nan        |
|   2 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-clang        |   61790.4        |   308954 |    5.00003 |         1 | base        | no         |      1 | nan        |
|   3 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-gcc          |   58194.3        |   290975 |    5.00006 |         2 | base        | no         |      1 | nan        |
|   4 | cpp              |          4 | BlackMark-pregenerated-inv_bits<u32>-gcc          |   24439.2        |   122197 |    5.00005 |         1 | base        | no         |      1 | nan        |
|   5 | cpp              |          3 | flo80_constexpr                                   |   16809.4        |    84048 |    5.00006 |         2 | base        | no         |      1 | nan        |
|   6 | cpp              |          3 | flo80_constexpr                                   |   14043.2        |    70217 |    5.00006 |         1 | base        | no         |      1 | nan        |
|   7 | rust             |          6 | SycrationMultithreaded                            |    4206.1        |    21095 |    5.01534 |         8 | base        | no         |    nan | nan        |
|   8 | rust             |          1 | mike-barber_bit-storage-striped                   |    3526.2        |    17633 |    5.00057 |         2 | base        | yes        |      1 | nan        |
|   9 | c                |          2 | danielspaangberg_5760of30030_epar                 |    3501.21       |    17509 |    5.00084 |         2 | wheel       | yes        |      1 | nan        |
|  10 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_bits<u32>-clang   |    3204.63       |    16024 |    5.00027 |         2 | wheel       | yes        |      1 | nan        |
|  11 | c                |          2 | danielspaangberg_480of2310_epar                   |    3143.07       |    15719 |    5.00115 |         2 | wheel       | yes        |      1 | nan        |
|  12 | rust             |          1 | mike-barber_bit-storage-striped-blocks            |    3136.47       |    15684 |    5.00052 |         2 | base        | yes        |      1 | nan        |
|  13 | rust             |          6 | SycrationSinglethreaded                           |    3123.07       |    15616 |    5.00021 |         1 | base        | no         |    nan | nan        |
|  14 | cpp              |          4 | BlackMark-5760of30030-os-hs-maskedbits<u32>-clang |    3013.18       |    15076 |    5.00336 |         2 | wheel       | yes        |      1 | nan        |
|  15 | cpp              |          4 | BlackMark-5760of30030-os-hs-maskedbits<u32>-gcc   |    2974.76       |    14875 |    5.0004  |         2 | wheel       | yes        |      1 | nan        |
|  16 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small      |    2792.8        |    13965 |    5.00036 |         2 | base        | yes        |      1 | nan        |
|  17 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_bits<u32>-gcc     |    2767.86       |    13841 |    5.00061 |         2 | wheel       | yes        |      1 | nan        |
|  18 | c                |          2 | danielspaangberg_48of210_epar                     |    2209.62       |    11052 |    5.00176 |         2 | wheel       | yes        |      1 | nan        |
|  19 | c                |          2 | danielspaangberg_5760of30030_owrb                 |    1948.53       |     9743 |    5.00017 |         1 | wheel       | yes        |      1 | nan        |
|  20 | c                |          3 | fvbakel_Cwords                                    |    1916.93       |     9585 |    5.00018 |         1 | other       | yes        |      1 | nan        |
|  21 | rust             |          1 | mike-barber_bit-storage-striped                   |    1832.71       |     9164 |    5.00024 |         1 | base        | yes        |      1 | nan        |
|  22 | c                |          2 | danielspaangberg_5760of30030_par                  |    1809.89       |     9050 |    5.00029 |         2 | wheel       | yes        |      1 | nan        |
|  23 | c                |          2 | danielspaangberg_480of2310_owrb                   |    1749.77       |     8749 |    5.0001  |         1 | wheel       | yes        |      1 | nan        |
|  24 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc      |    1683.81       |     8421 |    5.00116 |         2 | base        | yes        |      1 | nan        |
|  25 | c                |          1 | mckoss-c830                                       |    1668.2        |     8341 |    5       |         1 | wheel       | yes        |      1 | nan        |
|  26 | c                |          2 | danielspaangberg_480of2310_par                    |    1649.7        |     8249 |    5.00031 |         2 | wheel       | yes        |      1 | nan        |
|  27 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_bits<u32>-clang   |    1640.99       |     8205 |    5.00004 |         1 | wheel       | yes        |      1 | nan        |
|  28 | rust             |          1 | mike-barber_bit-storage-striped-blocks            |    1612.39       |     8063 |    5.00066 |         1 | base        | yes        |      1 | nan        |
|  29 | mixed            |          1 | ssovest-cgo                                       |    1601.4        |     8010 |    5.00186 |         1 | other       | no         |      1 | nan        |
|  30 | cpp              |          4 | BlackMark-5760of30030-os-hs-maskedbits<u32>-clang |    1561.5        |     7808 |    5.00033 |         1 | wheel       | yes        |      1 | nan        |
|  31 | cpp              |          4 | BlackMark-5760of30030-os-hs-maskedbits<u32>-gcc   |    1548.41       |     7743 |    5.0006  |         1 | wheel       | yes        |      1 | nan        |
|  32 | c                |          2 | danielspaangberg_48of210_par                      |    1511.5        |     7558 |    5.00032 |         2 | wheel       | yes        |      1 | nan        |
|  33 | c                |          2 | danielspaangberg_8of30_epar                       |    1474.03       |     7372 |    5.00124 |         2 | wheel       | yes        |      1 | nan        |
|  34 | rust             |          1 | mike-barber_bit-storage-striped-blocks-small      |    1442.08       |     7211 |    5.00042 |         1 | base        | yes        |      1 | nan        |
|  35 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_bits<u32>-gcc     |    1428.38       |     7142 |    5.00008 |         1 | wheel       | yes        |      1 | nan        |
|  36 | cython           |          1 | ssovest-cy                                        |    1400.16       |     7001 |    5.00014 |         1 | other       | yes        |      1 | nan        |
|  37 | c                |          2 | danielspaangberg_8of30_par                        |    1371.77       |     6859 |    5.00012 |         2 | wheel       | yes        |      1 | nan        |
|  38 | rust             |          1 | mike-barber_bit-storage                           |    1311.24       |     6558 |    5.00138 |         2 | base        | yes        |      1 | nan        |
|  39 | rust             |          1 | mike-barber_bit-storage-rotate                    |    1261.62       |     6310 |    5.00151 |         2 | base        | yes        |      1 | nan        |
|  40 | odin             |          1 | odin_bit_threaded_moe                             |    1220.91       |     6107 |    5.002   |         2 | base        | yes        |      1 | nan        |
|  41 | go               |          2 | ssovest-go-other-B                                |    1195.88       |     5980 |    5.0005  |         1 | other       | yes        |      1 | nan        |
|  42 | c                |          2 | danielspaangberg_48of210_owrb                     |    1174.16       |     5871 |    5.00017 |         1 | wheel       | yes        |      1 | nan        |
|  43 | c                |          2 | danielspaangberg_1of2_epar                        |    1161.8        |     5812 |    5.00257 |         2 | base        | yes        |      1 | nan        |
|  44 | c                |          2 | danielspaangberg_48of210                          |    1136          |     5681 |    5.00088 |         1 | wheel       | yes        |      1 | nan        |
|  45 | go               |          2 | ssovest-go-other                                  |    1109.89       |     5551 |    5.00138 |         1 | other       | yes        |      1 | nan        |
|  46 | cpp              |          2 | davepl_par                                        |    1069.69       |     5350 |    5.00143 |         2 | base        | yes        |      1 | nan        |
|  47 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_vec<u8>-gcc       |    1004.78       |     5025 |    5.0011  |         2 | wheel       | yes        |      8 | nan        |
|  48 | c                |          2 | danielspaangberg_8of30                            |     979.354      |     4897 |    5.00023 |         1 | wheel       | yes        |      1 | nan        |
|  49 | c                |          2 | danielspaangberg_1of2_par                         |     963.395      |     4817 |    5.00003 |         2 | base        | yes        |      1 | nan        |
|  50 | basic            |          3 | Nukepayload2_ArrayPool8of30M                      |     888.751      |     4444 |    5.00028 |         1 | wheel       | yes        |      1 | nan        |
|  51 | d                |          2 | BradleyChatha-MultistaticThreads-SieveCT          |     888.294      |     4443 |    5.00172 |         2 | base        | no         |      1 | nan        |
|  52 | basic            |          3 | Nukepayload2_ReDim8of30M                          |     872.54       |     4363 |    5.00035 |         1 | wheel       | yes        |      1 | nan        |
|  53 | d                |          2 | BradleyChatha-MultistaticThreads-SieveRT          |     840.077      |     4202 |    5.00192 |         2 | base        | yes        |      1 | nan        |
|  54 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-gcc      |     839.007      |     4196 |    5.00115 |         1 | base        | yes        |      1 | nan        |
|  55 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_vec<u8>-clang     |     827.806      |     4141 |    5.00238 |         2 | wheel       | yes        |      8 | nan        |
|  56 | rust             |          1 | mike-barber_byte-storage                          |     811.819      |     4061 |    5.00235 |         2 | base        | yes        |      8 | nan        |
|  57 | c                |          2 | danielspaangberg_8of30_owrb                       |     777.869      |     3890 |    5.00084 |         1 | wheel       | yes        |      1 | nan        |
|  58 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_arr<bool>-gcc            |     747.54       |     3740 |    5.00308 |         2 | base        | yes        |      8 | nan        |
|  59 | cython           |          1 | rpkak+bit-array                                   |     739.641      |     3699 |    5.00108 |         1 | base        | yes        |      1 | nan        |
|  60 | fortran          |          2 | tjol-bits                                         |     733.804      |     3670 |    5.00134 |         1 | base        | yes        |      1 | nan        |
|  61 | csharp           |          1 | kinematics_pool30m                                |     726.008      |     3631 |    5.00132 |         1 | wheel       | yes        |      1 | nan        |
|  62 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_arr<bool>-clang          |     710.652      |     3555 |    5.00245 |         2 | base        | yes        |      8 | nan        |
|  63 | cpp              |          4 | BlackMark-1of2-bs-hs-vec<u8>-clang                |     697.805      |     3490 |    5.0014  |         2 | base        | yes        |      8 | nan        |
|  64 | rust             |          1 | mike-barber_bit-storage                           |     673.009      |     3366 |    5.00142 |         1 | base        | yes        |      1 | nan        |
|  65 | odin             |          1 | odin_byte_threaded_moe                            |     670.398      |     3354 |    5.003   |         2 | base        | yes        |      8 | nan        |
|  66 | cpp              |          4 | BlackMark-1of2-bs-hs-vec<u8>-gcc                  |     662.937      |     3316 |    5.00198 |         2 | base        | yes        |      8 | nan        |
|  67 | rust             |          1 | mike-barber_bit-storage-rotate                    |     648.988      |     3245 |    5.00009 |         1 | base        | yes        |      1 | nan        |
|  68 | odin             |          1 | odin_bit_moe                                      |     625.4        |     3127 |    5       |         1 | base        | yes        |      1 | nan        |
|  69 | go               |          4 | kpym-go-multi                                     |     618.964      |     3095 |    5.00029 |         4 | base        | yes        |    nan | nan        |
|  70 | c                |          2 | danielspaangberg_1of2                             |     586.797      |     2934 |    5.00003 |         1 | base        | yes        |      1 | nan        |
|  71 | julia            |          2 | epithet-jl                                        |     580.381      |     2902 |    5.00016 |         1 | base        | yes        |      1 | nan        |
|  72 | nodejs           |          1 | rogiervandam                                      |     574.768      |     2958 |    5.14642 |         2 | base        | yes        |      1 | nan        |
|  73 | d                |          2 | BradleyChatha-MultistaticThreads-SieveRT_8        |     549.817      |     2750 |    5.00166 |         2 | base        | yes        |      8 | nan        |
|  74 | cpp              |          1 | davepl_pol                                        |     531.686      |     2659 |    5.00107 |         1 | base        | yes        |      1 | nan        |
|  75 | kotlin           |          1 | jvm_kotlin_idiomatic_fast_multi                   |     526.8        |     2634 |    5       |         2 | base        | yes        |    nan | nan        |
|  76 | kotlin           |          1 | jvm_kotlin_traditional_multi                      |     524.8        |     2624 |    5       |         2 | base        | yes        |    nan | nan        |
|  77 | fortran          |          1 | johandweber_fortran                               |     523.895      |     2620 |    5.001   |         1 | base        | no         |      1 | nan        |
|  78 | assembly         |          1 | rbergen_x64uff_bitshift                           |     521.6        |     2608 |    5       |         1 | base        | no         |      1 | nan        |
|  79 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_vec<u8>-gcc       |     520.605      |     2604 |    5.00187 |         1 | wheel       | yes        |      8 | nan        |
|  80 | crystal          |          1 | marghidanu                                        |     515.951      |     2580 |    5.00047 |         1 | base        | yes        |      1 | nan        |
|  81 | csharp           |          1 | kinematics_pool30                                 |     508.716      |     2544 |    5.00083 |         1 | wheel       | yes        |      1 | nan        |
|  82 | haskell          |          1 | fatho/bitset_unchecked                            |     508.003      |     2541 |    5.00194 |         1 | base        | no         |      1 | nan        |
|  83 | kotlin           |          1 | jvm_kotlin_idiomatic_multi                        |     508          |     2540 |    5       |         2 | base        | yes        |    nan | nan        |
|  84 | go               |          2 | ssovest-go-ptr                                    |     503.731      |     2519 |    5.00068 |         1 | base        | yes        |      1 | nan        |
|  85 | go               |          2 | ssovest-go-ptr-B                                  |     502.531      |     2514 |    5.00267 |         1 | base        | yes        |      1 | nan        |
|  86 | assembly         |          1 | rbergen_x64uff_bitbtr                             |     496.901      |     2485 |    5.001   |         1 | base        | no         |      1 | nan        |
|  87 | cpp              |          4 | BlackMark-5760of30030-os-hs-inv_vec<u8>-clang     |     495.645      |     2479 |    5.00156 |         1 | wheel       | yes        |      8 | nan        |
|  88 | assembly         |          1 | rbergen_x64ff_bitshift                            |     485.303      |     2427 |    5.001   |         1 | base        | yes        |      1 | nan        |
|  89 | julia            |          1 | dcbi                                              |     483.819      |     2420 |    5.00187 |         1 | base        | yes        |      1 | nan        |
|  90 | go               |          2 | ssovest-go-uint32-B                               |     479.487      |     2398 |    5.00118 |         1 | base        | yes        |      1 | nan        |
|  91 | assembly         |          1 | rbergen_x64ff_bitbtr                              |     472.306      |     2362 |    5.001   |         1 | base        | yes        |      1 | nan        |
|  92 | julia            |          3 | louie-github_port_1of2                            |     471.727      |     2359 |    5.00077 |         1 | base        | yes        |      1 | nan        |
|  93 | csharp           |          1 | kinematics_pool2of6                               |     460.653      |     2304 |    5.0016  |         1 | wheel       | yes        |      1 | nan        |
|  94 | cpp              |          4 | BlackMark-1of2-bs-hs-vec<u8>-gcc                  |     458.629      |     2294 |    5.00186 |         1 | base        | yes        |      8 | nan        |
|  95 | haskell          |          1 | fatho/bitset                                      |     456.119      |     2281 |    5.00089 |         1 | base        | no         |      1 | nan        |
|  96 | d                |          2 | BradleyChatha-Single-SieveCT                      |     447.598      |     2238 |    5.00002 |         1 | base        | no         |      1 | nan        |
|  97 | assembly         |          1 | rbergen_x64uff_byte                               |     441.2        |     2206 |    5       |         1 | base        | no         |      8 | nan        |
|  98 | nodejs           |          1 | rogiervandam_memcopy                              |     428.874      |     2145 |    5.00147 |         1 | other       | yes        |      1 | nan        |
|  99 | rust             |          1 | mike-barber_byte-storage                          |     427.586      |     2139 |    5.0025  |         1 | base        | yes        |      8 | nan        |
| 100 | d                |          2 | BradleyChatha-Single-SieveRT                      |     422.337      |     2112 |    5.00075 |         1 | base        | yes        |      1 | nan        |
| 101 | lua              |          2 | ben1jen_luajit1                                   |     420          |     2100 |    5       |         1 | base        | no         |      1 | nan        |
| 102 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_arr<bool>-clang          |     418.265      |     2092 |    5.00161 |         1 | base        | yes        |      8 | nan        |
| 103 | nim              |          2 | beef331                                           |     416.302      |     2082 |    5.00118 |         1 | base        | yes        |      1 | nan        |
| 104 | go               |          2 | ssovest-go-uint8-B                                |     416.165      |     2081 |    5.00042 |         1 | base        | yes        |      1 | nan        |
| 105 | go               |          2 | ssovest-go-uint8                                  |     410.602      |     2054 |    5.00241 |         1 | base        | yes        |      1 | nan        |
| 106 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_arr<bool>-gcc            |     410.194      |     2051 |    5.00007 |         1 | base        | yes        |      8 | nan        |
| 107 | cython           |          1 | rpkak+byte-array                                  |     397.244      |     1987 |    5.00196 |         1 | base        | yes        |      8 | nan        |
| 108 | go               |          2 | ssovest-go-uint32                                 |     396.939      |     1985 |    5.00076 |         1 | base        | yes        |      1 | nan        |
| 109 | dart             |          1 | eagerestwolf&mmcdon20_1bit_par                    |     393.287      |     1967 |    5.00144 |         2 | base        | yes        |      1 | nan        |
| 110 | cpp              |          4 | BlackMark-1of2-bs-hs-vec<u8>-clang                |     390.459      |     1953 |    5.00181 |         1 | base        | yes        |      8 | nan        |
| 111 | csharp           |          1 | kinematics_pool                                   |     373.492      |     1868 |    5.00145 |         1 | base        | yes        |      1 | nan        |
| 112 | fortran          |          2 | tjol-8bit                                         |     371.49       |     1858 |    5.00148 |         1 | base        | yes        |      8 | nan        |
| 113 | assembly         |          1 | rbergen_x64ff_byte                                |     363.927      |     1820 |    5.001   |         1 | base        | yes        |      8 | nan        |
| 114 | csharp           |          3 | tannergooding                                     |     358.369      |     1792 |    5.00043 |         1 | base        | yes        |      1 | nan        |
| 115 | csharp           |          1 | kinematics_raw32                                  |     349.431      |     1748 |    5.00242 |         1 | base        | yes        |      1 | nan        |
| 116 | odin             |          1 | odin_byte_moe                                     |     340.6        |     1703 |    5       |         1 | base        | yes        |      8 | nan        |
| 117 | scala            |          2 | scilari                                           |     318.936      |     1595 |    5.001   |         1 | base        | yes        |    nan | nan        |
| 118 | csharp           |          1 | kinematics_dbool                                  |     308.375      |     1542 |    5.00041 |         1 | base        | yes        |      8 | nan        |
| 119 | d                |          2 | BradleyChatha-Single-SieveRT_8                    |     306.593      |     1533 |    5.00012 |         1 | base        | yes        |      8 | nan        |
| 120 | csharp           |          1 | kinematics_ibool                                  |     304.829      |     1525 |    5.0028  |         1 | base        | yes        |      8 | nan        |
| 121 | java             |          1 | MansenC                                           |     303.679      |     1519 |    5.002   |         1 | base        | yes        |    nan | nan        |
| 122 | kotlin           |          1 | jvm_kotlin_idiomatic_fast_single                  |     295.744      |     1487 |    5.028   |         1 | base        | yes        |    nan | nan        |
| 123 | nodejs           |          1 | rogiervandam                                      |     292.487      |     1463 |    5.00193 |         1 | base        | yes        |      1 | nan        |
| 124 | dart             |          1 | eagerestwolf&mmcdon20_8bit_par                    |     280.565      |     1403 |    5.00062 |         2 | base        | yes        |      8 | nan        |
| 125 | csharp           |          1 | kinematics_raw                                    |     280.169      |     1401 |    5.00056 |         1 | base        | yes        |      1 | nan        |
| 126 | csharp           |          1 | kinematics_raw6                                   |     278.837      |     1395 |    5.00292 |         1 | wheel       | yes        |      1 | nan        |
| 127 | csharp           |          1 | kinematics_rawd                                   |     278.709      |     1394 |    5.00164 |         1 | base        | yes        |      1 | nan        |
| 128 | kotlin           |          1 | jvm_kotlin_idiomatic_single                       |     275.435      |     1378 |    5.003   |         1 | base        | yes        |    nan | nan        |
| 129 | kotlin           |          1 | jvm_kotlin_traditional_single                     |     271.034      |     1382 |    5.099   |         1 | base        | yes        |    nan | nan        |
| 130 | typescript       |          2 | mikevdbokke_32bit-array                           |     264          |     1320 |    5       |         1 | base        | yes        |      1 | nan        |
| 131 | csharp           |          1 | kinematics_bool                                   |     250.363      |     1252 |    5.00074 |         1 | base        | yes        |      8 | nan        |
| 132 | dart             |          1 | eagerestwolf&mmcdon20_8bit                        |     236.963      |     1185 |    5.00077 |         1 | base        | yes        |      8 | nan        |
| 133 | java             |          3 | MansenC-native                                    |     229.4        |     1147 |    5       |         1 | base        | yes        |    nan | nan        |
| 134 | typescript       |          2 | mikevdbokke_8bit-array                            |     223.4        |     1117 |    5       |         1 | base        | yes        |      1 | nan        |
| 135 | python           |          3 | emillynge_numpy                                   |     223.302      |     1117 |    5.00219 |         1 | base        | no         |      8 | nan        |
| 136 | basic            |          1 | rbergen_8of30                                     |     213          |     1065 |    5       |         1 | wheel       | yes        |      1 | nan        |
| 137 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-clang    |     212.468      |     1064 |    5.00781 |         2 | base        | yes        |      1 | nan        |
| 138 | scala            |          1 | rom1dep                                           |     211.673      |     1059 |    5.003   |         1 | base        | yes        |    nan | nan        |
| 139 | csharp           |          1 | kinematics_pool6p                                 |     208.053      |     1041 |    5.00353 |         2 | wheel       | yes        |      1 | nan        |
| 140 | dart             |          1 | eagerestwolf&mmcdon20_1bit                        |     206.511      |     1033 |    5.00216 |         1 | base        | yes        |      1 | nan        |
| 141 | basic            |          2 | rbergen_vb                                        |     187.942      |      940 |    5.00155 |         1 | base        | yes        |      1 | nan        |
| 142 | java             |          2 | PratimGhosh86-JavaBitSet                          |     177.6        |      888 |    5       |         1 | base        | yes        |      1 | nan        |
| 143 | fsharp           |          1 | rbergen                                           |     177.562      |      888 |    5.00107 |         1 | base        | yes        |      1 | nan        |
| 144 | csharp           |          1 | kinematics_standard                               |     177.368      |      887 |    5.0009  |         1 | base        | yes        |      1 | nan        |
| 145 | csharp           |          1 | kinematics_original                               |     168.825      |      845 |    5.00519 |         1 | base        | yes        |      1 | nan        |
| 146 | kotlin           |          1 | native_kotlin_idiomatic_fast_single               |     165.667      |      829 |    5.004   |         1 | base        | yes        |    nan | nan        |
| 147 | v                |          1 | marghidanu                                        |     159.4        |      797 |    5       |         1 | base        | yes        |    nan | nan        |
| 148 | ada              |          1 | BoopBeepBoopBeep                                  |     156.848      |      785 |    5.00484 |         1 | base        | no         |    nan | nan        |
| 149 | zig              |          1 | devblok                                           |     156.023      |      781 |    5.00566 |         1 | base        | yes        |      8 | nan        |
| 150 | kotlin           |          1 | native_kotlin_traditional_single                  |     153.585      |      769 |    5.007   |         1 | base        | yes        |    nan | nan        |
| 151 | csharp           |          2 | davepl                                            |     153.341      |      767 |    5.00194 |         1 | base        | yes        |      1 | nan        |
| 152 | haskell          |          1 | fatho/vector_unchecked                            |     151.117      |      756 |    5.00276 |         1 | base        | no         |      8 | nan        |
| 153 | haskell          |          1 | fatho/vector                                      |     150.442      |      753 |    5.00524 |         1 | base        | no         |      8 | nan        |
| 154 | assemblyscript   |          1 | donmahallem                                       |     150.37       |      752 |    5.001   |         1 | base        | yes        |    nan | nan        |
| 155 | pascal           |          1 | rbergen                                           |     147.4        |      737 |    5       |         1 | base        | yes        |    nan | nan        |
| 156 | fsharp           |          2 | dmannock_fsharp_port                              |     142.03       |      711 |    5.00597 |         1 | base        | yes        |    nan | nan        |
| 157 | fsharp           |          3 | dmannock_fsharp_recursion                         |     142.012      |      711 |    5.00662 |         1 | base        | yes        |    nan | nan        |
| 158 | nim              |          1 | marghidanu                                        |     140.999      |      705 |    5.00004 |         1 | base        | yes        |      8 | nan        |
| 159 | cobol            |          1 | fvbakel_Cobol                                     |     140.6        |      703 |    5       |         1 | base        | no         |      8 | nan        |
| 160 | csharp           |          1 | kinematics_rawp                                   |     138.302      |      692 |    5.00354 |         2 | base        | yes        |      1 | nan        |
| 161 | rust             |          2 | Azgrom                                            |     137.537      |      688 |    5.00227 |         1 | base        | yes        |    nan | nan        |
| 162 | d                |          1 | eagerestwolf                                      |     136.8        |      684 |    5       |         1 | base        | yes        |      8 | nan        |
| 163 | rust             |          4 | joshallen64                                       |     136.418      |      683 |    5.00665 |         1 | base        | yes        |    nan | nan        |
| 164 | kotlin           |          1 | native_kotlin_idiomatic_single                    |     135.465      |      678 |    5.005   |         1 | base        | yes        |    nan | nan        |
| 165 | typescript       |          2 | mikevdbokke_byte-array                            |     132.667      |      664 |    5.005   |         1 | base        | yes        |      8 | nan        |
| 166 | typescript       |          1 | marghidanu                                        |     131.921      |      660 |    5.003   |         1 | base        | yes        |    nan | nan        |
| 167 | pascal           |          2 | circular17                                        |     127.146      |      637 |    5.01    |         1 | base        | yes        |      1 | nan        |
| 168 | python           |          2 | ssovest                                           |     126.949      |      635 |    5.002   |         1 | base        | yes        |      8 | nan        |
| 169 | rust             |          3 | Blui42                                            |     120.386      |      602 |    5.00059 |         1 | base        | yes        |    nan | nan        |
| 170 | cpp              |          4 | BlackMark-1of2-cs-hs-inv_stridedbits<u8>-clang    |     108.691      |      544 |    5.005   |         1 | base        | yes        |      1 | nan        |
| 171 | pony             |          1 | marghidanu                                        |     104.6        |      523 |    5       |         1 | base        | yes        |      1 | nan        |
| 172 | go               |          1 | bundgaard                                         |     101.361      |      507 |    5.00193 |         1 | base        | yes        |    nan | nan        |
| 173 | fortran          |          2 | tjol-logical                                      |     100.768      |      504 |    5.00158 |         1 | base        | yes        |    nan | nan        |
| 174 | basic            |          1 | rbergen_boolean                                   |      93.6876     |      469 |    5.006   |         1 | base        | yes        |    nan | nan        |
| 175 | octave           |          1 | octave                                            |      63.2142     |      317 |    5.0147  |         1 | base        | no         |    nan | nan        |
| 176 | basic            |          1 | rbergen_bit64                                     |      50.8069     |      255 |    5.019   |         1 | base        | yes        |      1 | nan        |
| 177 | basic            |          1 | rbergen_bit32                                     |      50.3195     |      252 |    5.008   |         1 | base        | yes        |      1 | nan        |
| 178 | forth            |          1 | tjol-8bit                                         |      44.8699     |      225 |    5.01449 |         1 | base        | no         |      8 | nan        |
| 179 | haxe             |          1 | TayIorRobinson_Haxe_C++                           |      38.9351     |      195 |    5.00834 |         1 | base        | yes        |    nan | nan        |
| 180 | kotlin           |          1 | js_kotlin_idiomatic_fast_single                   |      37.7809     |      190 |    5.029   |         1 | base        | yes        |    nan | nan        |
| 181 | r                |          2 | nobrien97                                         |      36.1494     |      181 |    5.007   |         1 | base        | no         |     32 | nan        |
| 182 | kotlin           |          1 | js_kotlin_traditional_single                      |      35.8494     |      180 |    5.021   |         1 | base        | yes        |    nan | nan        |
| 183 | kotlin           |          1 | js_kotlin_idiomatic_single                        |      34.5444     |      174 |    5.037   |         1 | base        | yes        |    nan | nan        |
| 184 | ocaml            |          1 | gkpotter-faithful                                 |      33.8945     |      170 |    5.01556 |         1 | base        | yes        |    nan | nan        |
| 185 | r                |          1 | fvbakel_R                                         |      33.1337     |      166 |    5.01    |         1 | base        | yes        |     32 | nan        |
| 186 | ocaml            |          2 | gkpotter-unfaithful                               |      28.3855     |      142 |    5.00255 |         1 | base        | no         |    nan | nan        |
| 187 | idl              |          1 | kriztioan_idlway                                  |      23.6417     |      119 |    5.03349 |         1 | base        | yes        |      8 | nan        |
| 188 | forth            |          1 | tjol-1bit                                         |      14.8467     |       75 |    5.05164 |         1 | base        | no         |      1 | nan        |
| 189 | postscript       |          1 | epithet-ps                                        |      14.4354     |       73 |    5.057   |         1 | base        | no         |      8 | nan        |
| 190 | php              |          1 | DennisdeBest                                      |      12.7312     |       64 |    5.027   |         1 | base        | yes        |    nan | nan        |
| 191 | standardml       |          1 | NotMatthewGriffin_SMLofNJ                         |      12.4016     |       63 |    5.08    |         1 | base        | yes        |      1 | nan        |
| 192 | octave           |          2 | Brandon-Johns_8bit                                |      12.009      |       61 |    5.07952 |         1 | base        | yes        |      8 | nan        |
| 193 | scheme           |          1 | William103                                        |      11.6607     |       59 |    5.05972 |         1 | base        | yes        |      1 | nan        |
| 194 | typescript       |          2 | mikevdbokke_number-array                          |      11.1398     |       56 |    5.027   |         1 | base        | yes        |    nan | nan        |
| 195 | ruby             |          1 | rbergen                                           |       7.48768    |       38 |    5.075   |         1 | base        | yes        |    nan | nan        |
| 196 | wren             |          1 | marghidanu                                        |       7.10163    |       36 |    5.06926 |         1 | base        | yes        |    nan | nan        |
| 197 | ballerina        |          1 | da-strange-boi                                    |       7          |       35 |    5       |         1 | base        | yes        |      1 | no         |
| 198 | kos              |          1 | cdragan                                           |       6.68178    |       34 |    5.08846 |         1 | base        | yes        |      8 | nan        |
| 199 | gdscript         |          1 | OrigamiDev-Pete                                   |       4.88579    |       40 |    8.187   |         1 | base        | yes        |      8 | nan        |
| 200 | prolog           |          1 | jimbxb-prolog-c                                   |       4.00993    |       21 |    5.237   |         1 | base        | no         |      1 | nan        |
| 201 | perl             |          2 | kjetillll                                         |       3.72557    |       19 |    5.09989 |         1 | base        | yes        |    nan | nan        |
| 202 | lisp             |          1 | mikehw                                            |       3.07518    |       31 |   10.0807  |         1 | base        | no         |      1 | nan        |
| 203 | smalltalk        |          1 | fvbakel_smalltalk                                 |       2.97796    |       15 |    5.037   |         1 | base        | yes        |      1 | nan        |
| 204 | lua              |          1 | lua                                               |       2.8        |       14 |    5       |         1 | base        | no         |     64 | nan        |
| 205 | rexx             |          2 | joss_NetRexx                                      |       2.76384    |       14 |    5.06542 |         1 | base        | yes        |      8 | nan        |
| 206 | elixir           |          2 | thomas9911                                        |       2.38839    |       13 |    5.443   |         1 | base        | yes        |      1 | nan        |
| 207 | tex              |          2 | jfbu-tex-480of2310                                |       2.37579    |       12 |    5.05096 |         1 | wheel       | no         |    nan | nan        |
| 208 | perl             |          1 | marghidanu                                        |       2.36751    |       12 |    5.06862 |         1 | base        | yes        |    nan | nan        |
| 209 | mixal            |          1 | rbergen                                           |       2.34742    |       30 |   12.78    |         1 | base        | no         |      1 | nan        |
| 210 | tcl              |          2 | fvbakel_ootcl2                                    |       2.17005    |       11 |    5.069   |         1 | base        | yes        |     32 | nan        |
| 211 | rexx             |          1 | joss_REXX                                         |       1.7491     |        9 |    5.14549 |         1 | base        | no         |      8 | nan        |
| 212 | haxe             |          1 | TayIorRobinson_Haxe_HaxeEval                      |       1.5875     |        8 |    5.03936 |         1 | base        | yes        |    nan | nan        |
| 213 | python           |          1 | davepl                                            |       1.46306    |        8 |    5.46799 |         1 | base        | yes        |    nan | nan        |
| 214 | emojicode        |          1 | marghidanu                                        |       1.4        |        7 |    5       |         1 | base        | yes        |    nan | nan        |
| 215 | tex              |          2 | jfbu-tex                                          |       0.944635   |        5 |    5.29305 |         1 | base        | no         |    nan | nan        |
| 216 | powershell       |          2 | crowbar27_ps2                                     |       0.720917   |        4 |    5.54849 |         1 | base        | yes        |      1 | nan        |
| 217 | red              |          1 | mmcdon20_red                                      |       0.423957   |        3 |    7.07619 |         1 | base        | yes        |      1 | nan        |
| 218 | tcl              |          1 | fvbakeltcl                                        |       0.381971   |        2 |    5.236   |         1 | base        | yes        |      1 | nan        |
| 219 | raku             |          1 | draco1006                                         |       0.368348   |        2 |    5.42965 |         1 | base        | yes        |    nan | nan        |
| 220 | prolog           |          1 | jimbxb-prolog-dynamic                             |       0.368256   |        2 |    5.431   |         1 | base        | no         |    nan | nan        |
| 221 | sql              |          1 | fvbakel_sqlite                                    |       0.362106   |        2 |    5.52325 |         1 | other       | no         |      8 | nan        |
| 222 | haxe             |          1 | TayIorRobinson_Haxe_Python                        |       0.331753   |        2 |    6.02859 |         1 | base        | yes        |    nan | nan        |
| 223 | sql              |          2 | fvbakel_MariaDB3                                  |       0.31954    |        2 |    6.259   |         1 | other       | no         |     32 | nan        |
| 224 | tcl              |          2 | fvbakel_ootcl                                     |       0.304229   |        2 |    6.574   |         1 | base        | yes        |      1 | nan        |
| 225 | sql              |          2 | fvbakel_MariaDB2                                  |       0.184196   |        1 |    5.429   |         1 | other       | no         |     32 | nan        |
| 226 | idl              |          1 | kriztioan_1bit                                    |       0.181522   |        1 |    5.50896 |         1 | base        | yes        |      1 | nan        |
| 227 | bash             |          1 | bash_inline                                       |       0.127046   |        1 |    7.87116 |         1 | base        | no         |    nan | nan        |
| 228 | bash             |          1 | bash                                              |       0.07057    |        1 |   14.1703  |         1 | base        | no         |    nan | nan        |
| 229 | sql              |          2 | fvbakel_MariaDB1                                  |       0.051023   |        1 |   19.599   |         1 | base        | no         |     32 | nan        |
| 230 | tex              |          1 | tjol                                              |       0.0349945  |        1 |   28.5759  |         1 | base        | no         |     32 | nan        |
| 231 | bash             |          1 | bash_packed                                       |       0.0325755  |        1 |   30.6979  |         1 | base        | no         |    nan | nan        |
| 232 | prolog           |          1 | jimbxb-prolog-basic                               |       0.0315418  |        1 |   31.704   |         1 | base        | yes        |      1 | nan        |
| 233 | elixir           |          1 | cdesch                                            |       0.0114316  |        1 |   87.477   |         1 | base        | no         |    nan | nan        |
| 234 | powershell       |          1 | crowbar27_ps1                                     |       0.00348177 |        1 |  287.21    |         1 | base        | yes        |      1 | nan        |
| 235 | octave           |          2 | Brandon-Johns_1bit                                |       0.00120693 |        1 |  828.549   |         1 | base        | yes        |      1 | nan        |

## Test details


### Cpu

|                | Value                        |
|:---------------|:-----------------------------|
| manufacturer   | AMD                          |
| brand          | Athlon(tm) II Dual-Core M320 |
| vendor         | AuthenticAMD                 |
| family         | 16                           |
| model          | 6                            |
| stepping       | 2                            |
| revision       |                              |
| voltage        |                              |
| speed          | 0.8                          |
| speedMin       | 0.8                          |
| speedMax       | 2.1                          |
| governor       | schedutil                    |
| cores          | 2                            |
| physicalCores  | 2                            |
| processors     | 1                            |
| socket         |                              |
| virtualization | True                         |
| cache.l1d      | 131072                       |
| cache.l1i      | 131072                       |
| cache.l2       | 1                            |
| cache.l3       |                              |

|       | Value                                                                                                                                                                                                                                                                                                                                                                                 |
|:------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flags | fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm 3dnowext 3dnow constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid pni monitor cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a 3dnowprefetch osvw ibs skinit wdt hw_pstate vmmcall npt lbrv svm_lock nrip_save |

### OS

|             | Value             |
|:------------|:------------------|
| platform    | linux             |
| distro      | Ubuntu            |
| release     | 21.04             |
| codename    | Hirsute Hippo     |
| kernel      | 5.11.0-16-generic |
| arch        | x64               |
| codepage    | UTF-8             |
| logofile    | ubuntu            |
| build       |                   |
| servicepack |                   |
| uefi        | False             |

### System

|              | Value                 |
|:-------------|:----------------------|
| manufacturer | ASUSTeK Computer Inc. |
| model        | K70AF                 |
| version      | 1.0                   |
| sku          | -                     |
| virtual      | False                 |

## Docker

|                 | Value             |
|:----------------|:------------------|
| kernelVersion   | 5.11.0-16-generic |
| operatingSystem | Ubuntu 21.04      |
| osVersion       | 21.04             |
| osType          | linux             |
| architecture    | x86_64            |
| ncpu            | 2                 |
| memTotal        | 4117913600        |
| serverVersion   | 20.10.7           |
