from time import sleep
from selenium import webdriver


navegador = webdriver.Chrome()
navegador.get('https://externo.proway.com.br/login-aluno')
sleep(5)

navegador.find_element('xpath', '//*[@id="formLoginSubscriber_username"]').send_keys('vinereisch522@gmail.com')
navegador.find_element('xpath', '//*[@id="formLoginSubscriber_password"]').send_keys('27012006')
navegador.find_element('xpath', '//*[@id="formLoginSubscriber"]/div[3]/div/div/div/button').click()
sleep(1)
navegador.find_element('xpath', '/html/body/div[1]/section/section/main/div/div/div/ul/li[1]/ul/li/button').click()
sleep(1)
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_hoje"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_instrutorMetodologia"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_instrutorPostura"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_instrutorDominio"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_empresaAmbiente"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_empresaMicro"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_empresaRecepcao"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_obs"]').send_keys('Otimo professor, ensinando automação pros alunos')
