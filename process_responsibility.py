from responsibility_pattern import StepOne, StepTwo, StepThree, RequestHandler


class ProcessResponsibility:

    @staticmethod
    def do():
        req = RequestHandler(arr=[], enriched=['init'])

        sp1 = StepOne()
        sp2 = sp1.set_next(StepTwo())
        sp3 = sp2.set_next(StepThree())

        # start pipeline
        sp1.handle(req)
