from responsibility_pattern import StepOne, StepTwo, StepThree, RequestHandler


class ProcessResponsibility:

    @staticmethod
    def do():
        req = RequestHandler(enriched=['init'])

        sp1 = StepOne()
        sp2 = sp1.set_next(StepTwo())
        sp2.set_next(StepThree())

        # start pipeline
        sp1.handle(req)
