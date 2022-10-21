import pendulum
from datetime import datetime
import glob
from PIL import Image
from numpy import asarray
import os

from airflow.models import DAG
from airflow.decorators import dag, task
from airflow import Dataset


KST = pendulum.timezone("Asia/Seoul")

#senario
# when interval image is updated, dag will run
VALID_EXT = ['jpg', 'png']
IMROOT = './dbfiles/'
INTERVAL = 100
args = {
    'owner': 'user_name',
}


@dag(
    dag_id='check_img',
    default_args = args,
    description = 'example dag',
    start_date=datetime(2022, 10, 10, tzinfo=KST),
    schedule=[Dataset(IMROOT)],
)
def check_img():
    @task()
    def get_img_roots():
        imdbfiles = []
        for ext in VALID_EXT:
            imdbfiles += glob.glob(IMROOT + f'*.{ext}')

        if len(imdbfiles) > INTERVAL:
            tmp = []
            for dbf in imdbfiles:
                with open(dbf, 'r') as f:
                    tmp += f.readlines()
                os.remove(dbf)
            return tmp
        else:
            #no more rerun
            #TODO: log를 남기지 않도록???
            raise Exception('not enough image collected')


    @task()
    def check_image_extension(rootlist):
        tmp = []
        for root in rootlist:
            ext = root.split('.')[-1]
            tmp.append(
                {
                    'root': root,
                    'extension': ext, 
                    'is_image': ext in VALID_EXT
                }
            )

        return tmp


    @task()
    def print_img_size(xargs):
        for xarg in xargs:
            if xarg['is_image']:
                image = Image.open(xarg['root'])
                data = asarray(image)
                print(f"INFO: {xarg['root']}, {data.shape}")
            else:
                print(f'ERROR: invalid image {xarg["root"]}')

    
    impwdlist = get_img_roots(IMDBFILE)
    meta = check_image_extension(impwdlist)
    print_img_size(meta)

check_img() 