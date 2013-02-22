# Copyright cybertk. kyan.ql.he@gmail.com
{
  'variables': {
    'faac_version' : '1.28',

    'conditions': [
      ['OS == "linux"', {
        'use_system_faac%': 1,
      }, {
        'use_system_faac%': 0,
      }],
    ],
  },

  'conditions': [
    ['use_system_faac == 1', {
      'targets': [
        {
          'target_name': 'faac',
          'type': 'none',
          'link_settings': {
            'libraries': [
              '-lfaac',
            ],
          },
        }, # target
      ],
    }, { # else: use_system_faac != 1
      'targets': [
        {
          'target_name': 'faac',
            # TODO(kyan): Provide shared_library support.
          'type': 'static_library',

          'direct_dependent_settings': {
            'include_dirs': [
              'files/faac-<(faac_version)/include',
            ],
            'defines': [
            ],
          }, # direct_dependent_settings

          'msvs_settings': {
            'VCCLCompilerTool': {
              'CompileAs': '1',
              #'DisableSpecificWarnings': '4996',
            },
            'VCLibrarianTool': {
            }
          }, # msvs_settings

          'include_dirs': [
            'files/faac-<(faac_version)/include',
          ],

          'sources': [
            './files/faac-1.28/libfaac/bitstream.c',
            './files/faac-1.28/libfaac/tns.c',
            './files/faac-1.28/libfaac/frame.c',
            './files/faac-1.28/libfaac/fft.c',
            './files/faac-1.28/libfaac/channels.c',
            './files/faac-1.28/libfaac/ltp.c',
            './files/faac-1.28/libfaac/util.c',
            './files/faac-1.28/libfaac/kiss_fft/kiss_fftr.c',
            './files/faac-1.28/libfaac/kiss_fft/kiss_fft.c',
            './files/faac-1.28/libfaac/psychkni.c',
            './files/faac-1.28/libfaac/aacquant.c',
            './files/faac-1.28/libfaac/filtbank.c',
            './files/faac-1.28/libfaac/huffman.c',
            './files/faac-1.28/libfaac/midside.c',
            './files/faac-1.28/libfaac/backpred.c',
          ], # sources

          'conditions': [
            [ 'OS == "win"', {
              'defines': [
                '_LIB',
              ],
            }],
          ], # conditions
        },
      ]
    }], # conditions
  ],
}
