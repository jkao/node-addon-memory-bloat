{
  "targets": [{
    "target_name": "bloat",
    "sources": [
      "./bloat.cc",
      "./my-object.cc"
    ],
    "defines": [
    ],
    "include_dirs": [
      "<!@(node -p \"require('node-addon-api').include\")",
    ],
    'conditions': [
      ['OS=="linux"', {
        'cflags!': [ '-fno-exceptions' ],
        'cflags_cc!': [ '-fno-exceptions' ],
        'cflags': [
           '-Wno-sign-compare',
           '-Wno-type-limits',
           '-Wno-comment',
           '-Wno-bool-compare',
           '-Wno-extra',
        ],
        "cflags+": [
          "-std=c++11"
        ],
        "cflags_c+": [
          "-std=c++14"
        ],
        "cflags_cc+": [
          "-std=c++14"
        ],
      }],
      ['OS=="mac"', {
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          'OTHER_CPLUSPLUSFLAGS':[
            '-Wno-unused-private-field',
            '-Wno-sign-compare',
            '-stdlib=libc++',
            '-std=c++14',
          ],
        },

      }]
    ]
  }]
}
