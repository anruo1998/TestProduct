from pathlib import Path

class PollyPath:
    root_path = Path(__file__).parent.parent

    common_path = root_path / 'common'
    configs_path = root_path / 'configs'
    pageObjects_path = root_path / 'pageObjects'
    testCase_path = root_path / 'testCases'
    utile_path = root_path / 'utils'
    testDatas_path = root_path / 'testDatas'
    reports_path = root_path / 'outFiles'