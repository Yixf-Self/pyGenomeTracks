import matplotlib as mpl
mpl.use('agg')
from matplotlib.testing.compare import compare_images
from tempfile import NamedTemporaryFile
import os.path
import pygenometracks.plotTracks

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/test_data/"

tracks = """

[test bedgraph tabix]
file = epilog.qcat.bgz
height = 5
title = height=5

[spacer]

[x-axis]
"""

with open(ROOT + "epilogos.ini", 'w') as fh:
    fh.write(tracks)

tolerance = 13  # default matplotlib pixed difference tolerance


def test_narrow_track():
    region = "X:3100000-3150000"
#    region = "X:3000000-3130000"
    outfile = NamedTemporaryFile(suffix='.png', prefix='bedgraph_test_', delete=False)
    args = "--tracks {root}/epilogos.ini --region {region} --trackLabelFraction 0.2 " \
           "--dpi 130 --outFileName  {outfile}".format(root=ROOT, outfile=outfile.name, region=region).split()
    pygenometracks.plotTracks.main(args)
    print("saving test to {}".format(outfile.name))
    res = compare_images(ROOT + '/master_epilogos.png', outfile.name, tolerance)
    assert res is None, res

    os.remove(outfile.name)