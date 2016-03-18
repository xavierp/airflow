import logging

from airflow.models import DagRun
from airflow.operators import TriggerDagRunOperator
from airflow import settings


class TriggerMultipleDagRunOperator(TriggerDagRunOperator):
    """
    Triggers mutiple DAG runs for a specified ``dag_id`` if a criteria is met.

    :param trigger_dag_id: the dag_id to trigger
    :type trigger_dag_id: str
    :param python_callable: a reference to a python function that will be
        called while passing it the ``context`` object.
        If you want DagRuns created your function must return an iterable
        containing DagRunOrders. A DagRunOrder object contains a ``run_id`` and
        ``payload`` attribute that you can modify in your function.
        The ``run_id`` should be a unique identifier for that DAG run, and
        the payload has to be a picklable object that will be made available
        to your tasks while executing that DAG run. Your function header
        should look like ``def foo(context):``
    :type python_callable: python callable
    """

    def execute(self, context):
        dros = self.python_callable(context)

        if dros:
            session = settings.Session()
            for dro in dros:
                dr = DagRun(
                    dag_id=self.trigger_dag_id,
                    run_id=dro.run_id,
                    conf=dro.payload,
                    external_trigger=True)
                logging.info("Creating DagRun {}".format(dr))
                session.add(dr)
            session.commit()
            session.close()
        else:
            logging.info("Criteria not met, moving on")
