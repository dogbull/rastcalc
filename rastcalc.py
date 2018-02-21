import os

import rasterio

os.environ.update({
    'GDAL_HTTP_UNSAFESSL': 'YES',
})


def main():
    uri = 'https://s3.ap-northeast-2.amazonaws.com/parkjh/gis/dem.1000m.tiff'
    r = rasterio.open(uri)
    data = r.read(1, masked=True)

    print(r.profile)
    print('min:{}, max:{}'.format(data.min(), data.max()))


if __name__ == '__main__':
    main()
