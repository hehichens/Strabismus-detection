# Strabismus-detection

to detect the strabismus in the vedio


### by你的头发还好吗

## [Hichens](https://github.com/hehichens/Strabismus-detection/tree/master/hichens)
.
├── hichens
│   ├── dat
│   │   ├── dlib_face_recognition_resnet_model_v1.dat
│   │   └── shape_predictor_68_face_landmarks.dat
│   ├── detect_eye
│   │   ├── detect_eye_feature.py
│   │   ├── detect_eye.py
│   │   └── eye_feature.py
│   ├── detect_face
│   │   ├── detect_face_feature.py
│   │   ├── detect_face.py
│   │   ├── face_feature.py
│   │   ├── face_recognition.py
│   │   └── face_test.py
│   ├── eye_track.py
│   ├── hichens.md
│   ├── images
│   │   ├── 10.jpg
│   │   ├── 11.jpg
│   │   ├── 12.jpg
│   │   ├── 13.jpg
│   │   ├── 15.jpg
│   │   ├── 16.jpg
│   │   └── 9.jpg
│   ├── import2video.py
│   ├── svm
│   │   ├── detector1.svm
│   │   └── detector.svm
│   ├── tools
│   │   ├── get_img.py
│   │   ├── my_HOG.py
│   │   └── video
│   ├── track
│   │   ├── detector1.svm
│   │   ├── track_eye.py
│   │   ├── track.py
│   │   ├── track_test.py
│   │   ├── track_train.py
│   │   └── track_video.py
│   ├── xml_test
│   │   ├── image_metadata_stylesheet.xsl
│   │   └── test.xml
│   └── xml_train
│       ├── image_metadata_stylesheet.xsl
│       └── train.xml
├── README.md
└── 一些资料
    └── python语法
        └── python入门笔记
            ├── 01-python-tools
            │   ├── 01.01-python-overview.ipynb
            │   ├── 01.02-ipython-interpreter.ipynb
            │   ├── 01.03-ipython-notebook.ipynb
            │   └── 01.04-use-anaconda.ipynb
            ├── 02-python-essentials
            │   ├── 02.01-a-tour-of-python.ipynb
            │   ├── 02.02-python-data-types.ipynb
            │   ├── 02.03-numbers.ipynb
            │   ├── 02.04-strings.ipynb
            │   ├── 02.05-indexing-and-slicing.ipynb
            │   ├── 02.06-lists.ipynb
            │   ├── 02.07-mutable-and-immutable-data-types.ipynb
            │   ├── 02.08-tuples.ipynb
            │   ├── 02.09-speed-comparison-between-list-&-tuple.ipynb
            │   ├── 02.10-dictionaries.ipynb
            │   ├── 02.11-sets.ipynb
            │   ├── 02.12-frozen-sets.ipynb
            │   ├── 02.13-how-python-assignment-works.ipynb
            │   ├── 02.14-if-statement.ipynb
            │   ├── 02.15-loops.ipynb
            │   ├── 02.16-list-comprehension.ipynb
            │   ├── 02.17-functions.ipynb
            │   ├── 02.18-modules-and-packages.ipynb
            │   ├── 02.19-exceptions.ipynb
            │   ├── 02.20-warnings.ipynb
            │   └── 02.21-file-IO.ipynb
            ├── 03-numpy
            │   ├── 03.01-numpy-overview.ipynb
            │   ├── 03.02-matplotlib-basics.ipynb
            │   ├── 03.03-numpy-arrays.ipynb
            │   ├── 03.04-array-types.ipynb
            │   ├── 03.05-array-calculation-method.ipynb
            │   ├── 03.06-sorting-numpy-arrays.ipynb
            │   ├── 03.07-array-shapes.ipynb
            │   ├── 03.08-diagonals.ipynb
            │   ├── 03.09-data-to-&-from-string.ipynb
            │   ├── 03.10-array-attribute-&-method-overview-.ipynb
            │   ├── 03.11-array-creation-functions.ipynb
            │   ├── 03.12-matrix-object.ipynb
            │   ├── 03.13-general-functions.ipynb
            │   ├── 03.14-vectorizing-functions.ipynb
            │   ├── 03.15-binary-operators.ipynb
            │   ├── 03.16-universal-functions.ipynb
            │   ├── 03.17-choose.ipynb
            │   ├── 03.18-array-broadcasting.ipynb
            │   ├── 03.19-reading-and-writing-arrays.ipynb
            │   ├── 03.20-structured-arrays.ipynb
            │   ├── 03.21-record-arrays.ipynb
            │   ├── 03.22-memory-maps.ipynb
            │   ├── 03.23-from-matlab-to-numpy.ipynb
            │   ├── notebook.tex
            │   ├── output_11_1.png
            │   ├── output_13_1.png
            │   ├── output_17_1.png
            │   ├── output_19_1.png
            │   ├── output_21_1.png
            │   ├── output_24_1.png
            │   ├── output_24_2.png
            │   ├── output_26_1.png
            │   ├── output_29_1.png
            │   ├── output_31_1.png
            │   ├── output_34_1.png
            │   ├── output_36_1.png
            │   ├── output_39_1.png
            │   ├── output_41_0.png
            │   ├── output_48_1.png
            │   ├── output_5_1.png
            │   ├── output_53_1.png
            │   ├── output_58_1.png
            │   ├── output_7_1.png
            │   └── output_9_1.png
            ├── 04-scipy
            │   ├── 04.01-scienticfic-python-overview.ipynb
            │   ├── 04.02-interpolation-with-scipy.ipynb
            │   ├── 04.03-statistics-with-scipy.ipynb
            │   ├── 04.04-curve-fitting.ipynb
            │   ├── 04.05-minimization-in-python.ipynb
            │   ├── 04.06-integration-in-python.ipynb
            │   ├── 04.07-ODEs.ipynb
            │   ├── 04.08-sparse-matrix.ipynb
            │   ├── 04.09-linear-algbra.ipynb
            │   ├── 04.10-sparse-linear-algebra.ipynb
            │   └── JANAF_CH4.txt
            ├── 05-advanced-python
            │   ├── 05.01-overview-of-the-sys-module.ipynb
            │   ├── 05.02-interacting-with-the-OS---os.ipynb
            │   ├── 05.03-comma-separated-values.ipynb
            │   ├── 05.04-regular-expression.ipynb
            │   ├── 05.05-datetime.ipynb
            │   ├── 05.06-sql-databases.ipynb
            │   ├── 05.07-object-relational-mappers.ipynb
            │   ├── 05.08-functions.ipynb
            │   ├── 05.09-iterators.ipynb
            │   ├── 05.10-generators.ipynb
            │   ├── 05.11-context-managers-and-the-with-statement.ipynb
            │   ├── 05.12-decorators.ipynb
            │   ├── 05.13-decorator-usage.ipynb
            │   ├── 05.14-the-operator-functools-itertools-toolz-fn-funcy-module.ipynb
            │   ├── 05.15-scope.ipynb
            │   ├── 05.16-dynamic-code-execution.ipynb
            │   └── my_database.sqlite
            ├── 06-matplotlib
            │   ├── 06.01-pyplot-tutorial.ipynb
            │   ├── 06.02-customizing-plots-with-style-sheets.ipynb
            │   ├── 06.03-working-with-text---basic.ipynb
            │   ├── 06.04-working-with-text---math-expression.ipynb
            │   ├── 06.05-image-tutorial.ipynb
            │   ├── 06.06-annotating-axes.ipynb
            │   ├── 06.07-legend.ipynb
            │   ├── 06.08-figures,-subplots,-axes-and-ticks.ipynb
            │   ├── 06.09-do-not-trust-the-defaults.ipynb
            │   ├── 06.10-different-plots.ipynb
            │   ├── artists_figure.png
            │   ├── artists_tree.png
            │   └── stinkbug.png
            ├── 07-interfacing-with-other-languages
            │   ├── 07.01-introduction.ipynb
            │   ├── 07-02-example.zip
            │   ├── 07.02-python-extension-modules.ipynb
            │   ├── 07.03-cython-part-1.ipynb
            │   ├── 07-03-fib.zip
            │   ├── 07.04-cython-part-2.ipynb
            │   ├── 07-04-extern.zip
            │   ├── 07.05-cython-part-3.ipynb
            │   ├── 07-05-particle.zip
            │   ├── 07.06-cython-part-4.ipynb
            │   ├── 07-06-cython-sum.zip
            │   ├── 07.07-profiling-with-annotations.ipynb
            │   ├── 07.08-ctypes.ipynb
            │   ├── fib_orig.c
            │   ├── fib_orig.html
            │   ├── fib_orig.png
            │   └── fib_orig.pyx
            ├── 08-object-oriented-programming
            │   ├── 08.01-oop-introduction.ipynb
            │   ├── 08.02-using-oop-model-a-forest-fire.ipynb
            │   ├── 08.03-what-is-a-object.ipynb
            │   ├── 08.04-writing-classes.ipynb
            │   ├── 08.05-special-method.ipynb
            │   ├── 08.06-properties.ipynb
            │   ├── 08.07-forest-fire-simulation.ipynb
            │   ├── 08.08-inheritance.ipynb
            │   ├── 08.09-super.ipynb
            │   ├── 08.10-refactoring-the-forest-fire-simutation.ipynb
            │   ├── 08.11-interfaces.ipynb
            │   ├── 08.12-public-private-special-in-python.ipynb
            │   └── 08.13-multiple-inheritance.ipynb
            ├── 09-theano
            │   ├── 09.01-introduction-and-installation.ipynb
            │   ├── 09.02-theano-basics.ipynb
            │   ├── 09.03-gpu-on-windows.ipynb
            │   ├── 09.04-graph-structures.ipynb
            │   ├── 09.05-configuration-settings-and-compiling-modes.ipynb
            │   ├── 09.06-conditions-in-theano.ipynb
            │   ├── 09.07-loop-with-scan.ipynb
            │   ├── 09.08-linear-regression.ipynb
            │   ├── 09.09-logistic-regression-.ipynb
            │   ├── 09.10-softmax-on-mnist.ipynb
            │   ├── 09.11-net-on-mnist.ipynb
            │   ├── 09.12-random-streams.ipynb
            │   ├── 09.13-modern-net-on-mnist.ipynb
            │   ├── 09.14-convolutional-net-on-mnist.ipynb
            │   ├── 09.15-tensor-basics.ipynb
            │   ├── 09.16-tensor-indexing.ipynb
            │   ├── 09.17-tensor-operator-and-elementwise-operations.ipynb
            │   ├── 09.18-tensor-nnet-.ipynb
            │   ├── 09.19-tensor-conv.ipynb
            │   ├── apply1.png
            │   ├── apply2.png
            │   ├── apply_no_opti.png
            │   ├── apply_opti.png
            │   ├── download_mnist.py
            │   └── load.py
            ├── 10-something-interesting
            │   ├── 10.01-maps-using-basemap.ipynb
            │   ├── 10.02-maps-using-cartopy.ipynb
            │   ├── 10.03-nba-data.ipynb
            │   ├── 10.04-louis-cha's-kungfu-world.ipynb
            │   ├── bangs.txt
            │   ├── kungfu.txt
            │   ├── names.txt
            │   └── _Player.py
            ├── 11-useful-tools
            │   ├── 11.01-pprint.ipynb
            │   ├── 11.02-pickle-and-cPickle.ipynb
            │   ├── 11.03-json.ipynb
            │   ├── 11.04-glob.ipynb
            │   ├── 11.05-shutil.ipynb
            │   ├── 11.06-gzip,-zipfile,-tarfile.ipynb
            │   ├── 11.07-logging.ipynb
            │   ├── 11.08-string.ipynb
            │   ├── 11.09-collections.ipynb
            │   └── 11.10-requests.ipynb
            ├── 12-pandas
            │   ├── 12.01-ten-minutes-to-pandas.ipynb
            │   ├── 12.02-series-in-pandas.ipynb
            │   └── 12.03-dataframe-in-pandas.ipynb
            ├── generate index.ipynb
            ├── generate_static_files.ipynb
            ├── generate_static_files.py
            ├── index.ipynb
            ├── index.md
            ├── payment.jpg
            └── README.md

26 directories, 228 files
