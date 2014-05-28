from expects import expect

from mamba import formatters, reporter

from spec.object_mother import *


with description(formatters.XUnitFormatter):

    with before.all:
        self.example_group = an_example_group()
        self.example = an_example()
        self.example_group.append(self.example)

        self.formatter = formatters.XUnitFormatter()
        self.reporter = reporter.Reporter(self.formatter)

        self.reporter.start()
        self.example_group.run(self.reporter)
        self.reporter.finish()

        self.root = self.formatter.root

    with context('when checking root'):
        with it('contains testsuites as tag name'):
            expect(self.root.tag).to.be.equal('testsuites')

        with it('contains mamba as name attribute'):
            expect(self.root.get('name')).to.be.equal('mamba')

        with it('contains total examples as tests attribute'):
            expect(self.root.get('tests')).to.be.equal('1')

        with it('contains failed examples as failures attribute'):
            expect(self.root.get('failures')).to.be.equal('0')

        with it('contains pending examples as disabled attribute'):
            expect(self.root.get('disabled')).to.be.equal('0')

        with it('contains duration as time attribute'):
            expect(self.root.get('time')).to.not_be.equal('0')

    with context('when checking example group'):
        with it('contains testsuite'):
            expect(self.root.find('testsuite')).to.not_be.none

        with it('contains example group subject for testsuite'):
            expect(self.root.find('testsuite').get('name')).to.be(IRRELEVANT_SUBJECT)

        with it('contains child examples as tests attribute'):
            expect(self.root.find('testsuite').get('tests')).to.be.equal('1')

        with it('contains duration as time attribute'):
            expect(self.root.get('time')).to.not_be.equal('0')

    with it('contains testcase for example'):
        expect(self.root.find('testsuite').find('testcase')).to.not_be.none

    with it('contains example group subject for testcase'):
        expect(self.root.find('testsuite').find('testcase').get('name')).to.be.equal(self.example.name)

